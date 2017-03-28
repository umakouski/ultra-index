#!/usr/bin/python
# -*- coding: utf-8 -*-
from sys import argv
from definitions import *
import matplotlib.pyplot as plt

if len(argv) < 2:
    print "Usage: ", argv[0], " <data_file.csv> [data_file_2.csv ...]"
    exit(1)


filename = argv[1]
f = open(filename, "r")
line = f.readline()

title1 = argv[1] + '   Trials number is: ' + str(len(line.split(","))-1)
print title1
print "x[i]  ---  y[i] --- sigm_lst[i] --- min_lst[i] --- max_lst[i]"


x = []
y = []
y_minus_sigm = []
y_plus_sigm = []
min_lst = []
max_lst = []
sigm_lst = []

line = f.readline()
# Calculate mean(y), dispersion, min, max for each data-line
while line:
    dataline = map(float, line.split(","))
    x.append(int(dataline.pop(0)))
    m = mean(dataline)
    s = sigm(dataline)
    y.append(m)
    y_minus_sigm.append(m - s)
    y_plus_sigm.append(m + s)
    min_lst.append(min(dataline))
    max_lst.append(max(dataline))
    sigm_lst.append(s)
    line = f.readline()

for i in range(len(x)):
    print x[i], " --- ", y[i], " --- ", sigm_lst[i], " --- ", min_lst[i], " --- ", max_lst[i]

fig = plt.figure()
plt.title(title1)
plt.ylabel("Ultrametricity coeff. value")
plt.xlabel("Dimension")
plt.plot(x,y,"red",x,y_minus_sigm, "blue", x, y_plus_sigm,"blue", x,min_lst,"black", x, max_lst, "black", x, sigm_lst, "green")
#plt.savefig("graph01.pdf", fmt="pdf")
plt.show()

'''
for t in range(trials):
    line = line + ",mu_" + str(t + 1)

f.write(line + "\n")

dim = []
d = dim_1
while d <= dim_2:
    dim.append(d)
    d = d + dim_s

for d in dim:
    line = str(d)
    for t in range(trials):
        mu = getUltraCoeff(d, vert, e=ps, prt=False)
        line = line + "," + str(mu)
    line = line + "\n"
    f.write(line)
'''
f.close()
print "Complete!"

