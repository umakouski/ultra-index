#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from definitions import *

# the quantity of samples
samples = 100

# approximation
e = 0.005

# dimentions
dim = [3, 10, 20, 30, 40, 50, 100, 1000]

d = dim[5] # current dimension
n = 0      # the number of isosceles triangles
s = 0.     # mean value

if len(argv) > 1:
    d = int(argv[1])
if len(argv) > 2:
    e = float(argv[2])

print '{0:4} {1:4}   {2:18}           {3:18} {4:18} {5:18}\
      '.format("#","Iso.","Ultrametr. coeff","d(x,y)","d(y,z)","d(x,z)")
for i in range(samples):
    x = setPoint(d)
    y = setPoint(d)
    z = setPoint(d)
    t = isIso(x, y, z, d, e)
    if t:
        n = n + 1
    s = s * i / (i + 1.) + t/(i + 1.)
    print '{0:4} {1:4} {2:18} {3:18} {4:18} {5:18}\
          '.format(i + 1, n, s, dM(x,y,d), dM(y,z,d), dM(x,z,d))


print "\nUltrametricity coefficient is: ", n, "/", samples, " = ", s
print "Hypercube diameter equals: ", dM(N,E,d)
#print  '\n {0} \n {1} \n {2}'.format(x,y,z)
'''
s = 0
for i in range(100000):
    x = randint(0,1)
    if x:
        s = s + 1
print s/100000.
'''

