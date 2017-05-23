#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from definitions import *

if len(argv) < 2:
    print "Usage: ", argv[0], " <dimention> [v-tomy] [samples] [dependency] [pointsize]"
    exit(1)

# default dimention
d = 100

# default v-tomy value (dichotomy, trichotomy, etc.)
v = 0

# default quantity of samples
samples = 100

# default dependency level
alfa = 0

# default approximation (pointsize)
e = 0.005

if len(argv) > 1:
    d = int(argv[1])
if len(argv) > 2:
    v = float(argv[2])
if len(argv) > 3:
    samples = int(argv[3])
if len(argv) > 4:
    alfa = float(argv[4])
if len(argv) > 5:
    e = float(argv[5])

run = getUltraCoeff2(d, v, samples, alfa, e, prt=True)

'''
s = 0
for i in range(100000):
    x = randint(0,1)
    if x:
        s = s + 1
print s/100000.
'''

