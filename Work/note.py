import os
import gzip
import math
import urllib.request

with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
    for line in f:
        pass
        #print(line, end='')


x = math.sqrt(10)

u = urllib.request.urlopen('http://www.python.org/')
data = u.read()