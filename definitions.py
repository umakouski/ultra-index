#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import random, randint
from math import sqrt, pow

# get random point of Euclidean hypercube with dimention = dim
def setPoint(dim):
    x = []
    for i in range(dim):
        x.append(random())
    return x

# get random point of Boolean (v-tomy) hypercube with dimension = dim
def setVertex(dim, v):
    x = []
    for i in range(dim):
        x.append(randint(0, v - 1))
    return x
        

# Euclidean distance between point x and y with dimention = dim
def dE(x, y, dim):
    dE = 0.
    for i in range(dim):
        dE = dE + (x[i] - y[i])**2
    return pow(dE,1./dim)

# Hamming distance
def dH(x, y, dim):
    dH = 0
    for i in range(dim):
        if (x[i] <> y[i]):
            dH = dH + 1
    return dH

# Distance specified as: d(x,y) = max{|xi - yi|}
def dM(x, y, dim):
    dM = abs(x[0] - y[0])
    for i in range(dim-1):
        if (abs(x[i+1] - y[i+1]) > dM):
            dM = abs(x[i+1] - y[i+1])
    return dM

# is triangle isosceles?
def isIso(x, y, z, dim, e):
    t = []
    t = [dE(x,y,dim), dE(y,z,dim), dE(x,z,dim)]
    t.sort()
    if t[1]/t[2] >= 1 - e:
        return 1
    else:
        return 0

# is triangle isosceles (in boolean hypercube case)?
def isIsoBool(x, y, z, dim, e):
    t = []
    t = [dH(x,y,dim), dH(y,z,dim), dH(x,z,dim)]
    t.sort()
    if t[0] == 0:
        return -1
    if 1. * t[1] / t[2] >= 1 - e:
        return 1
    else:
        return 0

# define "0" and "1" points for hypercube diameter calculation
N, E = [], []
for i in range(10000):
    N.append(0.)
    E.append(1.)

