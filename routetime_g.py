#!/bin/python

import requests

def routetime_g(lng1, lat1, lng2, lat2):

    duratn = -1
    coords = "origins=%s,%s&destinations=%s,%s" % (lat1, lng1, lat2, lng2)
    r = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?%s" % coords)
    r.raise_for_status()
    res = r.json()
    if res['status'] == 'OK':
      el0 = res['rows'][0]['elements'][0]
      if el0['status'] == 'OK':
        duratn = el0['duration']['value']

    return duratn


if __name__ == "__main__":
    """   For Testing   """
    import geocode_g as geog

    address1 = "1600 Pennsylvania Ave NW, Washington, DC 20500"
    address2 = "6th St & Market St, Philadelphia, PA 19106"
    try:
        addr1_ll = geog.geocode_g( address1 )
        addr2_ll = geog.geocode_g( address2 )

        print "Driving time between: "
        print address1 + ": ", addr1_ll
        print address2 + ": ", addr2_ll

        print "Travel time (secs): ", routetime_g( addr1_ll[0], addr1_ll[1], addr2_ll[0], addr2_ll[1] )
    except StopIteration as errmsg:
        print errmsg
    except RuntimeWarning as errmsg:
        print errmsg
