#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from definitions import *

if len(argv) < 5:
    print "Usage: ", argv[0], " <dimention_start> <dimention_end> <dimention_step> <vertex_value> [number_of_trials = 100] "
    exit(1)

dim_1 = int(argv[1])
dim_2 = int(argv[2])
dim_s = int(argv[3])
vert = int(argv[4])
trials = 100
ps = 0.005
 
if len(argv) > 5:
    trials = int(argv[5])


print "Dimension start: ", dim_1, "\nDimension end:   ", dim_2, "\nDimension step:  ", dim_s, \
          "\nVertex value:    ", vert, "\nNumber of trials:", trials, "\n\nProcessing data..."

filename = "validation_", dim_1, "-", dim_2, "-", dim_s, "_", vert, "_tr", trials, "_.csv"
f = open(filename, "w")

line = "Dim"
for i in range(trials):
    line.append("," + 2)
	
print line


'''
s = 0
for i in range(100000):
    x = randint(0,1)
    if x:
        s = s + 1
print s/100000.
'''

