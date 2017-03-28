#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from definitions import *

# default quantity of samples
samples = 100

# default approximation (pointsize)
e = 0.005

# default v-tomy value (dichotomy, trichotomy, etc.)
v = 0

# default dimention
d = 1000

if len(argv) > 1:
    d = int(argv[1])
if len(argv) > 2:
    v = float(argv[2])
if len(argv) > 3:
    e = float(argv[3])

run = getUltraCoeff(d, v, samples, e)

'''
s = 0
for i in range(100000):
    x = randint(0,1)
    if x:
        s = s + 1
print s/100000.
'''

