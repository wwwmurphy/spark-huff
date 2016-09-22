#!/bin/python

import requests
import string

def geocode_g( addr ):

    addr = addr.translate(string.maketrans(' ','+'))
    payload = {'address': addr}
    r = requests.get("http://maps.googleapis.com/maps/api/geocode/json", params=payload)
    r.raise_for_status()

    res = r.json()
    if res['status'] == 'OK':
      loc = res['results'][0]['geometry']['location']
      return loc['lng'], loc['lat']

    if res['status'] == 'OVER_QUERY_LIMIT':
      raise StopIteration('Over Query Limit')

    if res['status'] == 'ZERO_RESULTS' or res['status'] == 'NOT_FOUND':
      raise RuntimeWarning('Address Not Found')

    return 999, 999

if __name__ == "__main__":
    """   For Testing   """
    address = "1600 Pennsylvania Ave NW, Washington, DC 20500"
    print address + ":", geocode_g( address )

