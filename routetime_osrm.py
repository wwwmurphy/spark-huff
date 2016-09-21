#!/bin/python

import requests

def routetime_osrm(lng1, lat1, lng2, lat2):

    coords = "%s,%s;%s,%s" % (lng1, lat1, lng2, lat2)
    r = requests.get("http://router.project-osrm.org/route/v1/driving/%s" % coords)
    res = r.json()
    if r.status_code != requests.codes.ok:
      print "Stopping due to error response."
      print r.status_code
    if res['code'] == 'Ok':
      duration = res['routes'][0]['duration']
    else:
      duration = -1
    return duration


if __name__ == "__main__":

  print "Driving time between: \n" +\
        "333 Ravenswood Ave, Menlo Park, Ca. (37.4576055, -122.1766376)\n" +\
        "1095 University Dr, Menlo Park, Ca. (37.449431, -122.186366)"

  lat1 = "37.4576055"
  lng1 = "-122.1766376"
  lat2 = "37.449431"
  lng2 = "-122.186366"

  print "Travel time (secs): ", routetime_osrm( lng1, lat1, lng2, lat2 )

