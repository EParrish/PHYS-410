import sys
import csv

pipein = csv.reader(sys.stdin, delimiter='.')
commaout = csv.writer(sys.stdout, dialect=csv.excel)
for row in pipein:
  commaout.writerow(row)