#!/usr/bin/python

###this script is used to calculate the rdf of PS-P2VP micelle
from __future__ import division
import sys,os,subprocess
import string, math
import random
import linecache

rho = 3.0
delr = 0.1
f_xyz = open("rdf.xyz","r")  ##input file
f_dat = open("rdf.dat","w")

lx,ly,lz = 200.00,40.00,40.00
rxc,ryc,rzc = 0.00,0.00,0.00
np = 3086   ##bead number
maxbin = int(lx*2/delr)  ##apart the lamellae into thin slips

rxyz = []
for lines in f_xyz.readlines()[2:]:
    line = lines.split()
    rxyz.append(line)
f_xyz.close()

##calculate the center of molecules
for i in range(np):
    rxc = rxc + float(rxyz[i][1])
    ryc = ryc + float(rxyz[i][2])
    rzc = rzc + float(rxyz[i][3])
rxc = rxc/np
ryc = ryc/np
rzc = rzc/np

for i in range(np):
    rxyz[i][1] = float(rxyz[i][1]) - rxc + lx

numO = [None]*maxbin
numC = [None]*maxbin
nums = [None]*maxbin
for i in range(maxbin):
    numO[i] = 0
    numC[i] = 0
    nums[i] = 0

for i in range(np):
    bin_i = int(rxyz[i][1]/delr)
    if rxyz[i][0] == 'C':
    	 numC[bin_i] = numC[bin_i]+1
    else:
    	 numO[bin_i] = numO[bin_i]+1
    nums[bin_i] += 1

##calculate the volume density
#vol = ly*lz*delr
#for i in range(maxbin):	  
#    numO[i] = numO[i]/vol
#    numC[i] = numC[i]/vol
#    print >> f_dat, i*delr, numO[i], numC[i]

##calculate the number ratio
for i in range(maxbin):
    if nums[i] != 0:
       fraO = numO[i]/nums[i]
       fraC = numC[i]/nums[i]
       print >> f_dat, i*delr, fraO, fraC
f_dat.close()

exit
