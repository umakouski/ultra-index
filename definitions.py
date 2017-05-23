#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import random, randint
from math import sqrt, pow

# get random point of Euclidean hypercube with dimention = dim, if v == 0
# or get random point of Boolean (v-tomy) hypercube with dimension == dim
def setPoint(dim, v=0, alfa=0):
    x = []
    if v >= 2:
        for i in range(dim):
            x.append(randint(0, v - 1))
        return x
    elif (v < 2) and (alfa == 0):
        for i in range(dim):
            x.append(random())
        return x
    elif (alfa > 0) and (alfa <= 1):
        f_common = random()
        for i in range(dim):
            try_coord = random()
            if try_coord < alfa:
                x.append(f_common)
            else:
                x.append(random())
        return x  
    else:
        print "setPoint usage error: alfa should be from the range [0,1]"
        exit(1)

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
    #return pow(dE,1./dim)
    return (dE * 1./ dim)**(1./2)

# Hamming distance
def dH(x, y, dim):
    dH = 0
    for i in range(dim):
        if (x[i] <> y[i]):
            dH = dH + 1
    return dH*1./dim

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
    "Return: 1 - isosceles; 0 - not isosceles; -1 - degenerate;"
    t = []
# !!! return dE to dH after experiment !!!
    t = [dH(x,y,dim), dH(y,z,dim), dH(x,z,dim)]
    t.sort()
    if t[0] == 0:
        return -1
    if 1. * t[1] / t[2] >= 1 - e:
        return 1
    else:
        return 0

# Get Ultrametricity coefficient for ultrametric space with specified parameters
def getUltraCoeff(dim=2, vert=2, sampl=1000, e=0.005, prt=True):
    '''getUltraCoeff(dim=2, vert=2, sampl=100, e=0.005, prt=True) 
    Returns Ultrametrisity coefficient for discrete vert-tomy hypercybe or Euclidean hypercube if vert = 0.
    dim - dimension of metric space; vert - the number of values that vertex could possess; 
    sampl - the number of triangles to try; e - pointsize of triangle vertex;
    prt - print user output (True), or supress it (False)
    ''' 
    n = 0      # the number of isosceles triangles
    s = 0.     # mean value

    if prt:
        print '{0:4} {1:4}   {2:18}           {3:18} {4:18} {5:18}\
              '.format("#","Iso.","Ultrametr. coeff","d(x,y)","d(y,z)","d(x,z)")

    i = 0
    while i < sampl:
    #for i in range(sampl):
        if vert > 0:
            x = setVertex(dim, vert)
            y = setVertex(dim, vert)
            z = setVertex(dim, vert)
            t = isIsoBool(x, y, z, dim, e)
        else:
            x = setPoint(dim)
            y = setPoint(dim)
            z = setPoint(dim)
            t = isIso(x, y, z, dim, e)
        if t != -1:
            # just skip degenerate triangle
            if t == 1:
                n = n + 1
            s = s * i / (i + 1.) + t/(i + 1.)
            if prt & (vert > 0):
                print '{0:4} {1:4} {2:18} {3:18} {4:18} {5:18}\
                      '.format(i + 1, n, s, dH(x,y,dim), dH(y,z,dim), dH(x,z,dim))
            elif prt & (vert <= 0):
                print '{0:4} {1:4} {2:18} {3:18} {4:18} {5:18}\
                      '.format(i + 1, n, s, dE(x,y,dim), dE(y,z,dim), dE(x,z,dim))
                
            i = i + 1
    if prt & (vert > 1):
        print "\nUltrametricity coefficient is: ", n, "/", sampl, " = ", s
        print "Discrete Hypercube diameter equals: ", dH(N,E,dim)
        print  '\n {0} \n {1} \n {2}'.format(x,y,z)
    elif prt & (vert <= 1):
        print "\nUltrametricity coefficient is: ", n, "/", sampl, " = ", s
        print "Euclidean Hypercube diameter equals: ", dE(N,E,dim)
#        print  '\n {0} \n {1} \n {2}'.format(x,y,z)        
    return s

# Edition 2: Get Ultrametricity coefficient for ultrametric space with specified parameters
def getUltraCoeff2(dim=2, vert=2, sampl=1000, depend=0, e=0.005, prt=True):
    '''getUltraCoeff(dim=2, vert=2, sampl=1000, depend=0, e=0.005, prt=True) 
    Returns Ultrametrisity coefficient for discrete vert-tomy hypercybe or Euclidean hypercube if vert = 0.
    dim - dimension of metric space; 
    vert - the number of values that vertex could possess; 
    sampl - the number of triangles to try; 
    depend - dependency level between coordinates. from 0 (independ) to 1 (all comp equal); 
    e - pointsize of triangle vertex;
    prt - print user output (True), or supress it (False)
    ''' 
    n = 0      # the number of isosceles triangles
    s = 0.     # mean value

    if prt:
        print '{0:4} {1:4}   {2:18}           {3:18} {4:18} {5:18}\
              '.format("#","Iso.","Ultrametr. coeff","d(x,y)","d(y,z)","d(x,z)")

    i = 0
    while i < sampl:
        x = setPoint(dim, vert, depend)
        y = setPoint(dim, vert, depend)
        z = setPoint(dim, vert, depend)
        if vert > 1:
            t = isIsoBool(x, y, z, dim, e)
        else:
            t = isIso(x, y, z, dim, e)
        if t != -1:
            # the triangle is degenerate - skip it
            if t == 1:
                n = n + 1
            s = s * i / (i + 1.) + t/(i + 1.)
            if prt & (vert >= 2):
                print '{0:4} {1:4} {2:18} {3:18} {4:18} {5:18}\
                      '.format(i + 1, n, s, dH(x,y,dim), dH(y,z,dim), dH(x,z,dim))
            elif prt & (vert < 2):
                print '{0:4} {1:4} {2:18} {3:18} {4:18} {5:18}\
                      '.format(i + 1, n, s, dE(x,y,dim), dE(y,z,dim), dE(x,z,dim))
                
            i = i + 1
    if prt & (vert > 1):
        print "\nUltrametricity coefficient is: ", n, "/", sampl, " = ", s
        print "Discrete Hypercube diameter equals: ", dH(N,E,dim)
#        print  '\n {0} \n {1} \n {2}'.format(x,y,z)
    elif prt & (vert <= 1):
        print "\nUltrametricity coefficient is: ", n, "/", sampl, " = ", s
        print "Euclidean Hypercube diameter equals: ", dE(N,E,dim)
#        print  '\n {0} \n {1} \n {2}'.format(x,y,z)        
    return s


# define "0" and "1" points for hypercube diameter calculation
N, E = [], []
for i in range(1000000):
    N.append(0.)
    E.append(1.)

# get mean (expected) value from the list
def mean(lst):
    s = 0.
    for l in lst:
        s = s + l
    return s/len(lst)

# get sqrt of dispersion from the list
def sigm(lst):
    m = mean(lst)
    s = 0.
    for l in lst:
        s = s + (l - m)**2
    return (s/len(lst))**(1./2)

