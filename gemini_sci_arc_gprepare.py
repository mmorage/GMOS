#!/usr/bin/env


#________________________________________________
#
# mmora@astro.puc.cl / mmorage@gmail.com
#
#_________________________________________________


import os,sys
from os.path import join, getsize
import pyraf
from pyraf import iraf
from iraf import imutil,hselect
import astropy
from astropy.io import fits
from iraf import gemini,gmos,gprepare,gbias,gsflat



# ________[iraf parameters]__________________
yes   = 'yes'
no    = 'no'
INDEF = 'INDEF'
# ________[output files]__________________
bias  = "BIAS.fits"
flat  = "FLAT_TEST.fits"

path=os.getcwd()
print(path)


# ________[Directory loop, creating archive list]__________________
for root, dirs, files in os.walk('.'):
    if root.startswith('./GS-'):
        archivo_sci  = open(join(root,'SCIENCE.txt'),'w')
        archivo_arc  = open(join(root,'ARC.txt'),'w')
        archivo_gsci = open(join(root,'gSCIENCE.txt'),'w')
        archivo_garc = open(join(root,'gARC.txt'),'w')
        for f in files:
            if f.endswith("fits") and f.startswith('S'):
                hdu      = fits.open(f)
                OBJECT   = hdu[0].header['OBJECT']
                OBSTYPE  = hdu[0].header['OBSTYPE']
                DATALAB  = hdu[0].header['DATALAB']
                MASKNAME = hdu[0].header['MASKNAME']
        
                
                if OBSTYPE == 'OBJECT'  and MASKNAME == '0.5arcsec' and OBSTYPE !='Twilight' :
                    #print(join(root,f))
                    #print(os.getcwd())
                    archivo_sci.write(f+"\n")
                    archivo_gsci.write("g"+f+"\n")
                if OBSTYPE == 'ARC'  and MASKNAME == '0.5arcsec' and OBSTYPE !='CuAr' :
                    archivo_arc.write(f+"\n")
                    archivo_garc.write("g"+f+"\n") 
                    
        archivo_sci.close()
        archivo_arc.close()
        archivo_gsci.close()
        archivo_garc.close()



# ________[Directory loop, running gprepare on ARCs]__________________
            
for root, dirs, files in os.walk('.'):
    if root.startswith('./GS-'):
        if  'database' in dirs:
            dirs.remove('database')
        os.chdir(root)
        cwd2 = os.getcwd()
        print(cwd2)
        #iraf.imheader('@ARC.txt')
        #try:
        print(os.getcwd())
        iraf.cd(os.getcwd())
        if os.stat("ARC.txt").st_size == 0:
            iraf.cd(path)
        else:
            try:
                iraf.unlear(gprepare)
                
                iraf.gprepare(inimages='@ARC.txt',outimages='@gARC.txt',fl_addmdf=yes,logfile='gprepare_arc.txt')
            
            except:
                print(cwd2)
            iraf.cd(path)
            os.chdir(path)



# ________[Directory loop, running gprepare on SCIENCE archives]__________________            

for root, dirs, files in os.walk('.'):
    if root.startswith('./GS-'):
        if  'database' in dirs:
            dirs.remove('database')
        os.chdir(root)
        cwd2 = os.getcwd()
        print(cwd2)
        print(os.getcwd())
        iraf.cd(os.getcwd())

        if os.stat("SCIENCE.txt").st_size == 0:
            iraf.cd(path)
        else:
            try:
                iraf.unlear(gprepare)
                iraf.gprepare(inimages='@SCIENCE.txt',outimages='@gSCIENCE.txt',fl_addmdf=yes,logfile='gprepare_sci.txt')
            
            except:
                print(cwd2)
            iraf.cd(path)
            os.chdir(path)
        




