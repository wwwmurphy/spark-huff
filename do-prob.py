#!/bin/python

import argparse
import csv
import math
from operator import itemgetter

# File format is:
# seq,name,address,W1,W2,W3,W4,lng,lat
# Weighting value ranges:
#   W1 = 100 - 9900, in units of 100.
#   W2 = 100 - 9900, in units of 100.
#   W3 =   0 -  100, in units of   1.
#   W4 =   0 -   10, in units of   1.

# TODO  Parse CSV Header to get value locations so there's no hard-coding in the writerow() call.


class Attractiveness:
    def __init__(self,w1,w2,w3,w4):
        self.beta = 1.5
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4

    def ROI(self, tcost, beta=None):
        ''' Composite Attractiveness divided by travel cost with nonlinear travel decay.
        Beta makes longer travel times even more undesireable.
        'tcost' is travel cost in units of 0.1 seconds of travel time. '''
        # This weighting is just made-up bullshit for now.
        s = float(self.w1)/1000. * \
            float(self.w2)/1000. * \
            float(self.w3)/100.  * \
            float(self.w4)/10.

        beta = self.beta if beta is None else beta
        tcost = math.pow(tcost/10., beta)

        return s / tcost


def proc(finame, ftname):

  locs = []
  names = []
  addrs = []
  with open(finame, 'rt') as fi, open(ftname, 'rt') as ft:

    ficsv = csv.reader(fi)
    ftcsv = csv.reader(ft)
    next(ficsv) # skip header
    next(ftcsv) # skip header

    for row_db in ficsv:
      row_t = next(ftcsv)
      if row_t == None:
        break
      if int(row_db[0]) != int(row_t[0]):
        print("Fatal sequence correlation error.")
        sys.exit(0)

      ttime = float(row_t[1])
      atrk = Attractiveness(row_db[3],row_db[4],row_db[5],row_db[6])
      roi = atrk.ROI(ttime, beta=1.75)
      locs.append([row_db[0], roi, 0])
      names.append(row_db[1])
      addrs.append(row_db[2])

  print "There are %d locations." % len(locs)
  roi_sum = sum(x[1] for x in locs)
  #print roi_sum
  for x in  locs:
    x[2] = x[1]/roi_sum
  slocs = sorted(locs, key=itemgetter(1), reverse=True)
  #print slocs
  print "Top 20 most likely destinations:"
  for i in range(20):
    seq = int(slocs[i][0])
    name = names[seq-1]+'.'+' '*40
    addr = addrs[seq-1]
    print "%02d. %05.2f%%. %s %s." % (seq, round(slocs[i][2]*100., 2), name[0:40], addr)


if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='Calculate Huff Probabilty that '+ \
           'a person at given home location will visit each target location.')
  parser.add_argument('-d','--database', help='CSV filename', required=True)
  parser.add_argument('-t','--times', help='Travel Times filename', required=True)
  args = vars(parser.parse_args())

  proc( args['database'], args['times'] )
