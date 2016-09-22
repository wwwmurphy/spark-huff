#!/bin/python

import requests

def routetime_mq(lng1, lat1, lng2, lat2, key):

    coords = "origins=%s,%s&destinations=%s,%s" % (lat1, lng1, lat2, lng2)
    payload = {'key': key, 'from': '%s,%s'%(lat1,lng1), 'to': '%s,%s'%(lat2,lng2)}
    r = requests.get("http://www.mapquestapi.com/directions/v2/route", params=payload)
    r.raise_for_status()
    res = r.json()
    if res['info']['statuscode'] == 0:
      duratn = res['route']['time']
    else:
      duratn = -1

    return duratn


if __name__ == "__main__":
    """   For Testing   """
    import geocode_mq as geomq
    import os
    mykey = os.getenv('MAPQUEST_KEY', 'None')

    address1 = "1600 Pennsylvania Ave NW, Washington, DC 20500"
    address2 = "100 S Independence Mall W, Philadelphia, PA 19106"
    try:
        addr1_ll = geomq.geocode_mq( address1, mykey )
        addr2_ll = geomq.geocode_mq( address2, mykey )

        print "Driving time between: "
        print address1 + ": ", addr1_ll
        print address2 + ": ", addr2_ll

        print "Travel time (secs): ", routetime_mq( addr1_ll[0], addr1_ll[1], addr2_ll[0], addr2_ll[1], mykey )
    except StopIteration as errmsg:
        print errmsg
    except RuntimeWarning as errmsg:
        print errmsg
