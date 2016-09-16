#!/bin/python

import requests

def routetime_mq(lng1, lat1, lng2, lat2):

    key = '4hmYZIGuAZG0rjoysi4GG3tRKAlCsxGL'
    duratn = -1
    coords = "origins=%s,%s&destinations=%s,%s" % (lat1, lng1, lat2, lng2)
    payload = {'key': key, 'from': '%s,%s'%(lat1,lng1), 'to': '%s,%s'%(lat2,lng2)}
    r = requests.get("http://www.mapquestapi.com/directions/v2/route", params=payload)
    res = r.json()
    if r.status_code != requests.codes.ok:
      print "Stopping due to error response: %d" % (r.status_code)
    if res['info']['statuscode'] == 0:
      duratn = res['route']['time']

    return duratn


if __name__ == "__main__":

  print "Driving time between: \n" +\
        "333 Ravenswood Ave, Menlo Park, Ca. (37.4576055, -122.1766376)\n" +\
        "1095 University Dr, Menlo Park, Ca. (37.449431, -122.186366)"

  lat1 = "37.4576055"
  lng1 = "-122.1766376"
  lat2 = "37.449431"
  lng2 = "-122.186366"

  print "Travel time (secs): ", routetime_mq( lng1, lat1, lng2, lat2 )

