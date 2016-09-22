#!/bin/python

import requests
import string

def geocode_mq( addr, key ):

    addr = addr.translate(string.maketrans(' ','+'))
    payload = {'key': key, 'thumbMaps': False, 'location': addr}
    r = requests.get("https://www.mapquestapi.com/geocoding/v1/address", params=payload)
    r.raise_for_status()
    res = r.json()
    if res['info']['statuscode'] == 0:
        loc = res['results'][0]['locations'][0]
        qc = loc['geocodeQualityCode']
        if 'X' in qc:
            print "MapQuest Quality Code is: %s" % qc
            raise RuntimeWarning('Address Not Found')
        lng = loc['latLng']['lng']
        lat = loc['latLng']['lat']
    else:
        lng = 999
        lat = 999

    return lng, lat


if __name__ == "__main__":
    """   For Testing   """
    import os
    mykey = os.getenv('MAPQUEST_KEY', 'None')
    address = "1600 Pennsylvania Ave NW, Washington, DC 20500"
    print address + ":", geocode_mq( address, mykey )

