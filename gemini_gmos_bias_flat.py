#!/usr/bin/env

#______________________________________
#
# mmora@astro.puc.cl / mmorage@gmail.com 28.07.2021
#_______________________________________
import os,sys
import pyraf
from pyraf import iraf
from iraf import imutil,hselect
import astropy
from astropy.io import fits
from iraf import gemini,gmos,gprepare,gbias,gsflat


# ________[EDIT THEM: 'yes' / 'no']__________________
use_gprepare_bias = 'yes'
use_gprepare_flat = 'yes'
use_bias          = 'yes'
use_flat          = 'yes'

# ________[iraf parameters]__________________
yes   = 'yes'
no    = 'no'
INDEF = 'INDEF'

# ________[gsflat  parameters from gemini, gmos ]__________________

def gsflat(inflat,specflat,fl_slitcorr=no,slitfunc="",fl_keep=no,combflat="FLAT_comb",fl_over=yes,fl_trim=yes,fl_bias=yes,fl_dark=no,fl_qecorr=no,fl_fixpix=yes,fl_oversize=yes,fl_vardq=yes,fl_fulldq=yes,dqthresh=0.1,bias="bias_out.fits",dark="",key_exptime="EXPTIME",key_biassec="BIASSEC",key_datasec="DATASEC",rawpath="",sci_ext="SCI",var_ext="VAR",dq_ext="DQ",key_mdf="MASKNAME",mdffile="",mdfdir="gmos$data/",bpm="mask.fits",gaindb="default",gratingdb="gmos$data/GMOSgratings.dat",filterdb="gmos$data/GMOSfilters.dat",bpmfile="gmos$data/chipgaps.dat",refimage="",qe_refim="",fl_keep_qeim=yes,qe_corrpref="qecorr",qe_corrimage="",qe_data="gmosQEfactors.dat",qe_datadir="gmos$data/",sat="default",xoffset=INDEF,yoffset=INDEF,yadd=0.0,wave_limit=INDEF,fl_usegrad=no,fl_emis=no,nbiascontam="default",biasrows="default",minval=INDEF,fl_inter=yes,fl_answer=yes,fl_detec=yes,fl_seprows=yes,function="spline3",order="13,11,28",low_reject=3.0,high_reject=3.0,niterate=2,combine="average",reject="avsigclip",masktype="goodvalue",maskvalue=0.0,scale="mean",zero="none",weight="none",statsec="",lthreshold=INDEF,hthreshold=INDEF,nlow=1,nhigh=1,nkeep=0,mclip=yes,lsigma=3.0,hsigma=3.0,key_ron="RDNOISE",key_gain="GAIN",ron=3.5,gain=2.2,snoise="0.0",sigscale=0.1,pclip=-0.5,grow=0.0,ovs_flinter=yes,ovs_med=no,ovs_func="chebyshev",ovs_order="default",ovs_lowr=3.0,ovs_highr=3.0,ovs_niter=2,fl_double=no,nshuffle=0,logfile="",verbose=yes,status=0,scanfile="",mode="al"):
    

    iraf.gsflat(inflats=inflat,specflat=specflat,fl_slitcorr=no,slitfunc="",fl_keep=no,combflat="FLAT_comb",fl_over=yes,fl_trim=yes,fl_bias=yes,fl_dark=no,fl_qecorr=no,fl_fixpix=yes,fl_oversize=yes,fl_vardq=yes,fl_fulldq=yes,dqthresh=0.1,bias="bias_out.fits",dark="",key_exptime="EXPTIME",key_biassec="BIASSEC",key_datasec="DATASEC",rawpath="",sci_ext="SCI",var_ext="VAR",dq_ext="DQ",key_mdf="MASKNAME",mdffile="",mdfdir="gmos$data/",bpm="mask.fits",gaindb="default",gratingdb="gmos$data/GMOSgratings.dat",filterdb="gmos$data/GMOSfilters.dat",bpmfile="gmos$data/chipgaps.dat",refimage="",qe_refim="",fl_keep_qeim=yes,qe_corrpref="qecorr",qe_corrimage="",qe_data="gmosQEfactors.dat",qe_datadir="gmos$data/",sat="default",xoffset=INDEF,yoffset=INDEF,yadd=0.0,wave_limit=INDEF,fl_usegrad=no,fl_emis=no,nbiascontam="default",biasrows="default",minval=INDEF,fl_inter=yes,fl_answer=yes,fl_detec=yes,fl_seprows=yes,function="spline3",order="13,11,28",low_reject=3.0,high_reject=3.0,niterate=2,combine="average",reject="avsigclip",masktype="goodvalue",maskvalue=0.0,scale="mean",zero="none",weight="none",statsec="",lthreshold=INDEF,hthreshold=INDEF,nlow=1,nhigh=1,nkeep=0,mclip=yes,lsigma=3.0,hsigma=3.0,key_ron="RDNOISE",key_gain="GAIN",ron=3.5,gain=2.2,snoise="0.0",sigscale=0.1,pclip=-0.5,grow=0.0,ovs_flinter=yes,ovs_med=no,ovs_func="chebyshev",ovs_order="default",ovs_lowr=3.0,ovs_highr=3.0,ovs_niter=2,fl_double=no,nshuffle=0,logfile="",verbose=yes,status=0,scanfile="",mode="al")

    return()



#________[gprepare bias]__________________

if use_gprepare_bias == 'yes':
    archivo_bias=open('BIAS.txt','w')        

    files  =  [f for f in os.listdir('.') if os.path.isfile(f)]

    for f in files:
        if f.endswith(('.fits')) and f.startswith('S'):

            hdu      = fits.open(f)
            OBJECT   = hdu[0].header['OBJECT']
            OBSTYPE  = hdu[0].header['OBSTYPE']
            DATALAB  = hdu[0].header['DATALAB']
            MASKNAME = hdu[0].header['MASKNAME']
        
            if OBJECT == 'Bias' and OBSTYPE == 'BIAS' and MASKNAME == '0.5arcsec':
                #print(OBJECT,OBSTYPE,DATALAB,MASKNAME)
                #print(f)
                archivo_bias.write(f+"\n")
    archivo_bias.close()


    iraf.gprepare(inimages='@BIAS.txt')


#________[gbias]__________________
add_g=""

if use_bias=='yes':

    with open('BIAS.txt','r') as f:
        for line in f:
            add_g+='g'+line.strip()+"\n"
        f.close()
    with open('gBIAS.txt','w') as f:
        f.write(add_g)
        f.close()

    iraf.unlearn('gbias')
    iraf.gbias(inimages="@gBIAS.txt",outbias='BIAS.fits',logfile="gbias_logfile.txt",fl_over='yes',fl_trim='yes')



#________[gprepare flats]__________________

if use_gprepare_flat == 'yes':
    archivo_flat=open('FLAT.txt','w')        

    files  =  [f for f in os.listdir('.') if os.path.isfile(f)]

    for f in files:
        if f.endswith(('.fits')) and f.startswith('S'):

            hdu      = fits.open(f)
            OBJECT   = hdu[0].header['OBJECT']
            OBSTYPE  = hdu[0].header['OBSTYPE']
            DATALAB  = hdu[0].header['DATALAB']
            MASKNAME = hdu[0].header['MASKNAME']
        
            if OBJECT == 'GCALflat' and OBSTYPE == 'FLAT' and MASKNAME == '0.5arcsec':
                print(OBJECT,OBSTYPE,DATALAB,MASKNAME)
                print(f)
                archivo_flat.write(f+"\n")
    archivo_flat.close()
    iraf.gprepare(inimages='@FLAT.txt')




#________[gflats]__________________

add_g=""
if  use_flat == 'yes':  

    with open('FLAT.txt','r') as f:
        for line in f:
            add_g+='g'+line.strip()+"\n"
        f.close()
    with open('gFLAT.txt','w') as f:
        f.write(add_g)
        f.close()

        gsflat('@gFLAT.txt','FLAT_TEST.fits',fl_over=yes,fl_trim=yes,fl_bias=yes,fl_dark=no,fl_qecorr=no,fl_fixpix=yes,fl_oversize=yes,fl_vardq=yes,fl_fulldq=yes,dqthresh=0.1,bias="BIAS.fits",order=3,fl_inter=yes,ovs_flinter=yes,logfile='gflat_logfile.txt')
    
