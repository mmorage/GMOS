#!/usr/bin/env

#___________________________________________________

import os,sys
from os.path import join, getsize

import astropy
from astropy.io import fits

import pyraf
from pyraf import iraf
from iraf import gemini,gmos,gprepare,gbias,\
    gsflat,gsreduce,gswavelength,gstransform,\
    imutil,hselect


#________[iraf parameters]__________________
yes   = 'yes'
no    = 'no'
INDEF = 'INDEF'

path  = os.getcwd()

for root, dirs, files in os.walk('.'):
    if root.startswith('./GS-'):
        if 'database'in dirs:
            dirs.remove('database')
        os.chdir(root)
        cwd2=os.getcwd()
        #________[iraf/pyraf change of directory]__________________
        iraf.cd(os.getcwd())
        
        if os.stat("gARC.txt").st_size==0:
            iraf.cd(path)
        else:
            with open('gsgARC.txt','r') as f:
                for line in f:
                    calib_arc=line.strip()[:-5]
                    #print calib_arc
                f.close()
                local=os.getcwd()
                iraf.cd(local)
                print(local)
                print(calib_arc)

                iraf.gstransform(inimages="gsgS*.fits",fl_wavtran=yes,wavtraname=calib_arc,fl_vardq=yes,fl_flux=yes)

                #iraf.imheader(calib_arc)
                os.chdir(path) 
