#!/bin/python

import requests
import string

def geocode_g( addr ):

    addr = addr.translate(string.maketrans(' ','+'))
    payload = {'address': addr}
    r = requests.get("http://maps.googleapis.com/maps/api/geocode/json", params=payload)

    if r.status_code != requests.codes.ok:
      raise RuntimeError('Google: Stopping due to error response.')

    res = r.json()
    if res['status'] == 'OK':
      loc = res['results'][0]['geometry']['location']
      return loc['lng'], loc['lat']

    if res['status'] == 'OVER_QUERY_LIMIT':
      raise StopIteration('Google: Stopping due to Over Query Limit')

    if res['status'] == 'ZERO_RESULTS' or res['status'] == 'NOT_FOUND':
      raise RuntimeWarning('Google: Address Not Found')

    return 999, 999

if __name__ == "__main__":
    """   For Testing   """
    address = "1600 Pennsylvania Ave NW, Washington, DC 20500"
    print address + ":", geocode_g( address )

