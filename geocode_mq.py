#!/bin/python

import requests
import string

<<<<<<< HEAD
def geocode_mq( addr, key ):

    addr = addr.translate(string.maketrans(' ','+'))
    payload = {'key': key, 'thumbMaps': False, 'location': addr}
    r = requests.get("https://www.mapquestapi.com/geocoding/v1/address", params=payload)
    r.raise_for_status()
    res = r.json()
    if res['info']['statuscode'] == 0:
      loc = res['results'][0]['locations'][0]
      qc = loc['geocodeQualityCode']
      if 'X' in qc or qc[0:2] != 'L1':
        print "MapQuest Quality Code is: %s" % qc
        raise RuntimeWarning('MapQuest: Address Not Found')
      return loc['latLng']['lng'], loc['latLng']['lat']
=======
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
>>>>>>> 193f3a9edd89a3334ef5b2f8a88877bb7f783023

    return 999, 999


if __name__ == "__main__":
<<<<<<< HEAD
    """   For Testing   """
    import os
    mykey = os.getenv('MAPQUEST_KEY', 'None')
    address = "1600 Pennsylvania Ave NW, Washington, DC 20500"
    print address + ":", geocode_mq( address, mykey )

=======
    print "333 Ravenswood Ave, Menlo Park, Ca",
    print geocode_mq( "nonexistent, Menlo Park, Ca" )
>>>>>>> 193f3a9edd89a3334ef5b2f8a88877bb7f783023
