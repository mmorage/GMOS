#!/usr/bin/env

#____________________________________________________
#
# Quick data reduction. no qe, no wave calibration: 
# mmora@astro.puc.cl / mmorage@gmail.com
#____________________________________________________


import os,sys
from os.path import join, getsize
import pyraf
from pyraf import iraf
from iraf import imutil,hselect
import astropy
from astropy.io import fits
from iraf import gemini,gmos,gprepare,gbias,gsflat,gsreduce

#________[iraf parameters]__________________
yes   = 'yes'
no    = 'no'
INDEF = 'INDEF'

#________[load flat,bias]__________________

cwd  = os.getcwd()
path = os.getcwd()
FLAT = join(cwd,"FLAT_TEST.fits")
BIAS = join(cwd,"BIAS.fits")

#________[directory loop, running gsreduce on ARCs]__________________

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
            try:
                iraf.unlearn(gsreduce)
                print(os.getcwd())
                
                iraf.gsreduce(inimages="@gARC.txt" ,outimages="",outpref='gs',fl_over=yes,fl_trim=yes,fl_bias=yes,fl_gscrrej=yes,fl_crspec=no,fl_dark=no,fl_qecorr=no,fl_flat=no,fl_gmosaic=yes,fl_fixpix=yes,fl_gsappwave=yes,fl_scatsub=no,fl_cut=no,fl_title=no,fl_oversize=yes,fl_vardq=no,fl_fulldq=no,dqthresh=0.1,bias=BIAS,dark="",flatim=FLAT,geointer="linear",gradimage="",refimage="",qe_refim="",fl_keep_qeim=yes,qe_corrpref="qecorr",qe_corrimage="",qe_data="gmosQEfactors.dat",qe_datadir="gmos$data/",key_exptime="EXPTIME",key_biassec="BIASSEC",key_datasec="DATASEC",cr_xorder=9,cr_sigclip=4.5,cr_sigfrac=0.5,cr_objlim=1.0,cr_niter=4,fl_inter=no,rawpath="",sci_ext="SCI",var_ext="VAR",dq_ext="DQ",key_mdf="MASKNAME",mdffile="",mdfdir="gmos$data/",bpm="mask.fits",gaindb="default",gratingdb="gmos$data/GMOSgratings.dat",filterdb="gmos$data/GMOSfilters.dat",xoffset=INDEF,yoffset=INDEF,yadd=0.0,wave_limit=INDEF,bpmfile="gmos$data/chipgaps.dat",key_ron="RDNOISE",key_gain="GAIN",ron=3.5,gain=2.2,sat="default",key_nodcount="NODCOUNT",key_nodpix="NODPIX",ovs_flinter=no,ovs_med=no,ovs_func="chebyshev",ovs_order="default",ovs_lowr=3.0,ovs_highr=3.0,ovs_niter=2,nbiascontam="default",biasrows="default",sc_nfind=1,sc_column=INDEF,sc_torder=3,sc_order1="11",sc_sample1="*",sc_order2="7",sc_niterate2=3,logfile="",verbose=yes,status=0,scanfile1="",scanfile2="",mode="al")


                
            except:
                a=1
                #print(cwd2)
            iraf.cd(path)
            os.chdir(path) 



#________[directory loop, running gsreduce on SCIENCE]__________________

for root, dirs, files in os.walk('.'):
    if root.startswith('./GS-'):
        if 'database'in dirs:
            dirs.remove('database')
        os.chdir(root)
        cwd2=os.getcwd()
        iraf.cd(os.getcwd())
        
        if os.stat("gSCIENCE.txt").st_size==0:
            iraf.cd(path)
        else:
            try:
                iraf.unlear(gsreduce)
                print(os.getcwd())
                
                iraf.gsreduce(inimages="@gSCIENCE.txt" ,outimages="",outpref='gs',fl_over=yes,fl_trim=yes,fl_bias=yes,fl_gscrrej=yes,fl_crspec=no,fl_dark=no,fl_qecorr=no,fl_flat=yes,fl_gmosaic=yes,fl_fixpix=yes,fl_gsappwave=yes,fl_scatsub=no,fl_cut=no,fl_title=no,fl_oversize=yes,fl_vardq=yes,fl_fulldq=no,dqthresh=0.1,bias=BIAS,dark="",flatim=FLAT,geointer="linear",gradimage="",refimage="",qe_refim="",fl_keep_qeim=yes,qe_corrpref="qecorr",qe_corrimage="",qe_data="gmosQEfactors.dat",qe_datadir="gmos$data/",key_exptime="EXPTIME",key_biassec="BIASSEC",key_datasec="DATASEC",cr_xorder=9,cr_sigclip=4.5,cr_sigfrac=0.5,cr_objlim=1.0,cr_niter=4,fl_inter=no,rawpath="",sci_ext="SCI",var_ext="VAR",dq_ext="DQ",key_mdf="MASKNAME",mdffile="",mdfdir="gmos$data/",bpm="mask.fits",gaindb="default",gratingdb="gmos$data/GMOSgratings.dat",filterdb="gmos$data/GMOSfilters.dat",xoffset=INDEF,yoffset=INDEF,yadd=0.0,wave_limit=INDEF,bpmfile="gmos$data/chipgaps.dat",key_ron="RDNOISE",key_gain="GAIN",ron=3.5,gain=2.2,sat="default",key_nodcount="NODCOUNT",key_nodpix="NODPIX",ovs_flinter=no,ovs_med=no,ovs_func="chebyshev",ovs_order="default",ovs_lowr=3.0,ovs_highr=3.0,ovs_niter=2,nbiascontam="default",biasrows="default",sc_nfind=1,sc_column=INDEF,sc_torder=3,sc_order1="11",sc_sample1="*",sc_order2="7",sc_niterate2=3,logfile="",verbose=yes,status=0,scanfile1="",scanfile2="",mode="al")


                
            except:
                a=1
                #print(cwd2)
            iraf.cd(path)
            os.chdir(path) 
