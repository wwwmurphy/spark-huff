#!/bin/python

import argparse
import csv
import json
import math
import requests
import string
import time

import geocode_g

# File format is:
# seq,name,address,W1,W2,W3,W4,lng,lat

# TODO  Parse CSV Header to get value locations so there's no hard-coding in the writerow() call.
# TODO  Try geocoder at https://geocoder.opencagedata.com/
# TODO  Try geocoder at https://developer.mapquest.com/products/geocoding/


# Distance in kilometers.
def distance_onsphere(lat1,lng1, lat2,lng2):
  R = 6371 # km
  dLat = math.radians(lat2-lat1)
  dLon = math.radians(lng2-lng1)
  a = math.sin(dLat/2) * math.sin(dLat/2) + \
      math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
      math.sin(dLon/2) * math.sin(dLon/2)
  return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))


def proc(finame, foname):

  queryLimit = 2499
  queries = 0

  with open(finame, 'rb') as fi, open(foname, 'wb') as fo:
    focsv = csv.writer(fo)
    ficsv = csv.reader(fi)
    focsv.writerow(next(ficsv)) # CSV header pass thru
    for row in ficsv:
      addr = "%s" % (row[2])
      addr = addr.translate(string.maketrans(' ','+'))
      payload = {'address': addr}
      r = requests.get("http://maps.googleapis.com/maps/api/geocode/json", params=payload)
      print r.url
      if r.status_code != requests.codes.ok:
        print "Stopping due to error response from Google."
        break
      res = r.json()
      if res['status'] == 'OK':
        lat = res['results'][0]['geometry']['location']['lat']
        lng = res['results'][0]['geometry']['location']['lng']

      if res['status'] == 'OVER_QUERY_LIMIT':
        print "Stopping due to: " + res['status']
        break

      if res['status'] == 'ZERO_RESULTS' or res['status'] == 'NOT_FOUND':
        lat = 999
        lng = 999
      else:
        lng_old = float(row[7])
        lat_old = float(row[8])
        dist = distance_onsphere(round(float(lat),7),round(float(lng),7), lat_old,lng_old)
        print('Seq: %5d. Error: %.2f meters; %.2f feet; %.2f miles.' % \
             (int(row[0]), dist * 1000, dist * 3280.84, (dist * 3280.84) / 5280))

      focsv.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],lng,lat])

      queries = queries + 1
      if queries == queryLimit:
        break
      time.sleep(0.25) # don't hammer on the nice free server

  print "Completed %d queries." % queries


if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='Get updated Lat/long data for " + \
           "Store database. Program stops at 2500 updates or if server returns an error.')
  parser.add_argument('-d','--database', help='CSV filename', required=True)
  parser.add_argument('-o','--out', help='Output filename', required=True)
  args = vars(parser.parse_args())

  proc( args['database'], args['out'] )

