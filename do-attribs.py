#!/bin/python

import argparse
import random
import csv

# File format is:
# seq,name,address,W1,W2,W3,W4,lng,lat

# TODO  Parse CSV Header to get value locations so there's no hard-coding in the writerow() call.


def proc(finame, foname):

  recs = 0

  with open(finame, 'rb') as fi, open(foname, 'wb') as fo:
    focsv = csv.writer(fo)
    ficsv = csv.reader(fi)
    focsv.writerow(next(ficsv)) # CSV header pass thru
    for row in ficsv:

      w1 = str( int(random.uniform(1,99)) * 100)
      w2 = str( int(random.uniform(1,99)) * 100)
      w3 = str( int(random.uniform(0, 1)  * 100.))
      w4 = str( int(random.uniform(0, 1)  *  10.))
      focsv.writerow([row[0],row[1],row[2],w1,w2,w3,w4,row[7],row[8]])

      recs = recs + 1

  print "Completed %d records." % recs


if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='Generate random Attractiveness Values.')
  parser.add_argument('-d','--database', help='CSV filename', required=True)
  parser.add_argument('-o','--out', help='Output filename', required=True)
  args = vars(parser.parse_args())

  proc( args['database'], args['out'] )

