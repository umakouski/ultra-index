#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from definitions import *

if len(argv) < 5:
    print "Usage: ", argv[0], " <dimention_start> <dimention_end> <dimention_step> <vertex_value> \
[number_of_trials = 100] [dependency = 0] [pointsize = 0.005]"
    exit(1)

dim_1 = int(argv[1])
dim_2 = int(argv[2])
dim_s = int(argv[3])
vert = int(argv[4])
trials = 100
alfa = 0
ps = 0.005
 
if len(argv) > 5:
    trials = int(argv[5])
if len(argv) > 6:
    alfa = float(argv[6])
if len(argv) > 7:
    ps = float(argv[6])

print "Dimension start: ", dim_1, "\nDimension end:   ", dim_2, "\nDimension step:  ", dim_s, \
          "\nVertex value:    ", vert, "\nNumber of trials:", trials,\
          "\nDependency level: ", alfa, "\nPointsize:       ", ps, "\n\nProcessing data..."

if alfa == 0:
    filename = "data_"+str(dim_1)+"-"+str(dim_2)+"-"+str(dim_s)+"_v"+str(vert)+\
                                             "_dep0_tr"+str(trials)+"_.csv"
elif alfa ==1:
    filename = "data_"+str(dim_1)+"-"+str(dim_2)+"-"+str(dim_s)+"_v"+str(vert)+\
                                             "_dep1_tr"+str(trials)+"_.csv"
else:
    filename = "test0001.csv"

f = open(filename, "w")
line = "Dim"
for t in range(trials):
    line = line + ",mu_" + str(t + 1)

f.write(line + "\n")

dim = []
d = dim_1
while d <= dim_2:
    dim.append(d)
    d = d + dim_s

out0 = -1
for d in dim:
    line = str(d)
    for t in range(trials):
        mu = getUltraCoeff2(d, vert, depend=alfa, e=ps, prt=False)
        line = line + "," + str(mu)
    line = line + "\n"
    f.write(line)

    out = int(round(float(d - dim_1)*100/(dim_2 - dim_1)))
    if out > out0:
        out0 = out
        print out,"%"

f.close()
print "\nComplete!"
print "Output file is: ", filename
