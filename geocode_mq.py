#!/bin/python

import requests
import string

def geocode_mq( addr ):

    key = '4hmYZIGuAZG0rjoysi4GG3tRKAlCsxGL'
    addr = addr.translate(string.maketrans(' ','+'))
    payload = {'key': key, 'thumbMaps': False, 'location': addr}
    r = requests.get("https://www.mapquestapi.com/geocoding/v1/address", params=payload)

    if r.status_code != requests.codes.ok:
      raise RuntimeError('Stopping due to error response from Google.')

    res = r.json()
    if res['info']['statuscode'] == 0:
      lng = res['results'][0]['locations'][0]['latLng']['lng']
      lat = res['results'][0]['locations'][0]['latLng']['lat']
      return lng, lat

    else:
      print res['info']['messages']
      raise StopIteration('Stopping due to ....')

    #if res['status'] == 'ZERO_RESULTS' or res['status'] == 'NOT_FOUND':
    #  raise RuntimeWarning('Address Not Found')

    return 999, 999


if __name__ == "__main__":
    print "333 Ravenswood Ave, Menlo Park, Ca",
    print geocode_mq( "nonexistent, Menlo Park, Ca" )
