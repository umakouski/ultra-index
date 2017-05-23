#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from definitions import *

if len(argv) < 4:
    print "Usage: ", argv[0], " <dimention_start> <dimention_end> <dimention_step> [vertex_value] [number_of_trials = 100] "
    exit(1)

dim_1 = int(argv[1])
dim_2 = int(argv[2])
dim_s = int(argv[3])
vert = 0
trials = 100

if len(argv) > 4:
    vert = int(argv[4])
if len(argv) > 5:
    trials = int(argv[5])


print "Dimension start: ", dim_1, "\nDimension end:   ", dim_2, "\nDimension step:  ", dim_s, \
          "\nVertex value:    ", vert, "\nNumber of trials:", trials, "\n\nProcessing data..."

filename = "validation_" + str(dim_1) + "-" + str(dim_2) + "-" + str(dim_s) + "_v" \
            + str(vert) + "_tr" + str(trials) + "_.csv"
f = open(filename, "w")

line = "Dim"
for i in range(trials):
    line = line + ",d" + str(i)
f.write(line + "\n")

dim = []
d = dim_1
while d <= dim_2:
    dim.append(d)
    d = d + dim_s

perc0 = -1
for d in dim:
    line = str(d)
    # for defined number of trials get 2 random points and measure the distance
    for t in range(trials):
        if vert < 2:
            x = setPoint(d)
            y = setPoint(d)
            line = line + "," + str(dE(x,y,d))
        else:
            x = setPoint(d,vert)
	    y = setPoint(d,vert)
            line = line + "," + str(dH(x,y,d))
    line = line + "\n"
    f.write(line)
    
    perc = int(round(float(d - dim_1)*100/(dim_2 - dim_1)))
    if perc > perc0:
        perc0 = perc
        print "\r", perc, "%"

f.close()
print "\nComplete!"
print "Output file is: ", filename
'''
s = 0
for i in range(100000):
    x = randint(0,1)
    if x:
        s = s + 1
print s/100000.
'''

