#!/usr/bin/env python

#
# Sort gemini data. Get the program data from the archive 
#
# Then run:  python GS-NNNN-sort.py > archive.csh
#      
#
# requires Gemini_code_program.xml  from the OT (export the program)
#
#
#
# It reads all ODBs from the xml, creating a directory per Group


#####################################################
# 21.July.2021 mmora@astro.puc.cl / mmorage@gmail.com
#####################################################


import xml.etree.ElementTree as ET
import os,sys,string
import numpy as np
from lxml.etree import parse as lparse
from  pandas import *


valor2 =  []
files  =  [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
    if f.endswith(('.xml')):
         
        ltree =  lparse(f)
        tree  =  ET.parse(f)     #setup ETread
        root  =  tree.getroot() #define root
        
        #for some_value_name in ltree.findall("//value"):
        for value in ltree.findall("//paramset"):
            
            valor = []
            
            if  value.attrib["name"] =="dataset":
                for b in value.iter("param"):
                    try:
                        valor.append(b.attrib["value"])
                    except:
                        o = 0
                valor2.append(valor)   

valor3   = sorted(valor2,key = lambda x:x[1])                
ARCHIVOS = np.asarray(DataFrame(np.asarray(valor3)).drop_duplicates().values)


for i in range(len(ARCHIVOS)):
    text  = "mkdir "+str(ARCHIVOS[i,0])[:-4]  
    text2 = "cp "+str(ARCHIVOS[i,1])+".fits "+str(ARCHIVOS[i,0])[:-4]+"/."    
    print(text)
    print(text2)

#deleting empty directories from not observed ODBs
print("rmdir *")
