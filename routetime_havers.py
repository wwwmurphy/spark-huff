#!/bin/python

# The purpose of this module is to provide a quick n' dirty method to simulate
# distance calculations without actually hitting on any Restful APIs on the
# internet that either cost money, are rate limited or are slow.
# Consequently, the answers returned here are completely inaccurate. They will
# have a passing resemblance to reality and will exhibit a proportionality
# to the correct value.


import math

# Haversine formula
# Distance in kilometers.
def distance_onsphere(lat1,lng1, lat2,lng2):
  R = 6371 # km
  lat1 = float(lat1)
  lat2 = float(lat2)
  lng1 = float(lng1)
  lng2 = float(lng2)
  dLat = math.radians(lat2-lat1)
  dLon = math.radians(lng2-lng1)
  a = math.sin(dLat/2) * math.sin(dLat/2) + \
      math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
      math.sin(dLon/2) * math.sin(dLon/2)
  return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1-a))


def routetime_havers(lng1, lat1, lng2, lat2):

    duratn = distance_onsphere(lat1,lng1, lat2,lng2)

    duratn = duratn * 0.621371  # convert to miles
    duratn = duratn / 20        # convert to hours at 20 MPH
    duratn = duratn * 3600      # convert to seconds

    return int(duratn)


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

        print "Travel time (secs): ", routetime_havers( addr1_ll[0], addr1_ll[1], addr2_ll[0], addr2_ll[1] )
    except StopIteration as errmsg:
        print errmsg
    except RuntimeWarning as errmsg:
        print errmsg
