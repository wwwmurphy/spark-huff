#!/bin/python

import requests

def routetime_g(lng1, lat1, lng2, lat2):

    duratn = -1
    coords = "origins=%s,%s&destinations=%s,%s" % (lat1, lng1, lat2, lng2)
    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?%s" % coords)
    res = r.json()
    if r.status_code != requests.codes.ok:
      print "Stopping due to error response: %d" % (r.status_code)
    if res['status'] == 'OK':
      el0 = res['rows'][0]['elements'][0]
      if el0['status'] == 'OK':
        duratn = el0['duration']['value']

    return duratn


if __name__ == "__main__":

  print "Driving time between: \n" +\
        "333 Ravenswood Ave, Menlo Park, Ca. (37.4576055, -122.1766376)\n" +\
        "1095 University Dr, Menlo Park, Ca. (37.449431, -122.186366)"

  lat1 = "37.4576055"
  lng1 = "-122.1766376"
  lat2 = "37.449431"
  lng2 = "-122.186366"

  print "Travel time (secs): ", routetime_g( lng1, lat1, lng2, lat2 )

