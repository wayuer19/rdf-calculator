#!/usr/bin/python

###this script is used to calculate the rdf of PS-P2VP micelle
import sys,os,subprocess
import string, math
import random
import linecache

rho = 3.0
delr = 0.2
f_xyz = open("rdf.xyz","r")
f_dat = open("rdf.dat","w")

lx,ly,lz = 40.00,40.00,40.00
rxc,ryc,rzc = 0.00,0.00,0.00
np = 11520
maxbin = int(lx/2/delr)

rxyz = []
for lines in f_xyz.readlines()[2:]:
    line = lines.split()
    rxyz.append(line)
f_xyz.close()

for i in range(np):
    rxc = rxc + float(rxyz[i][1])
    ryc = ryc + float(rxyz[i][2])
    rzc = rzc + float(rxyz[i][3])
rxc = rxc/np
ryc = ryc/np
rzc = rzc/np

numO = [None]*maxbin
numC = [None]*maxbin
numS = [None]*maxbin
for i in range(maxbin):
    numO[i] = 0
    numC[i] = 0
    numS[i] = 0

for i in range(np):
    rxij = float(rxyz[i][1])-rxc
    ryij = float(rxyz[i][2])-ryc
    rzij = float(rxyz[i][3])-rzc
    rij = math.sqrt(rxij**2+ryij**2+rzij**2)
    dist = int(rij/delr)
    
    if rxyz[i][0] == 'O':
    	 numO[dist] = numO[dist]+1
    elif rxyz[i][0] == 'C':
    	 numC[dist] = numC[dist]+1
    else:
    	 numS[dist] = numS[dist]+1

pi = math.pi
const = 4.0*pi/3.0
for i in range(maxbin):
    rlow = i*delr
    rup = rlow + delr
    r = rlow + delr*0.5
    vol = const*(rup**3-rlow**3)
	  
    numO[i] = numO[i]/vol
    numC[i] = numC[i]/vol
    numS[i] = numS[i]/vol
    print >> f_dat, r, numO[i], numC[i], numS[i]

f_dat.close()

exit
