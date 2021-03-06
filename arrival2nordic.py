#!/usr/bin/env python

from obspy.core import UTCDateTime
from datetime import timedelta
import random
import sys

if len(sys.argv)<2:
    print 'No input files'
    sys.exit()

def randomdate(startdate, enddate):
	return startdate + random.random() * (enddate - startdate) 

def create_sfile(arrivalP, arrivalS, date):
    year = str(date.year)
    if len(str(date.month)) < 2:
        month = '0'+str(date.month)
    else:  
        month = str(date.month)
    if len(str(date.day)) < 2:
        day = '0'+str(date.day)
    else:  
        day = str(date.day)
    if len(str(date.hour)) < 2:
        hour = '0'+str(date.hour)
    else:  
        hour = str(date.hour)
    if len(str(date.minute)) < 2:
        minute = '0'+str(date.minute)
    else:  
        minute = str(date.minute)
    if len(str(date.second)) < 2:
        second = '0'+str(date.second)
    else:  
        second = str(date.second)

    S = open(day+'-'+hour+minute+'-'+second+'L.S'+year+month, 'w')
    S.write(' '+year+' '+month+day+' '+hour+minute+' '+second+'.0'+' L                                                         1\n')
    S.write(' ACTION:REG 15-11-17 19:58 OP:xxx  STATUS:               ID:'+year+month+day+hour+minute+second+'     I\n')
    S.write(' STAT SP IPHASW D HRMM SECON CODA AMPLIT PERI AZIMU VELO AIN AR TRES W  DIS CAZ7\n')
    for STA in arrivalP:
        S.write(' '+STA+' EZ E'+arrivalP[STA][1]+'       '+hour+minute+' '+str(round(float(arrivalP[STA][0]), 2))+'\n')
    for STA in arrivalS:
        S.write(' '+STA+' EZ E'+arrivalS[STA][1]+'       '+hour+minute+' '+str(round(float(arrivalS[STA][0]), 2))+'\n')
    S.close()
   
   


min = timedelta(minutes=1)
arrivals = open(sys.argv[1], 'r').readlines()
starttime = UTCDateTime(2015, 01, 01)


for i in range(1, int(arrivals[-2].split()[0]) + 1):
	arr_dic_P = {}
	arr_dic_S = {}
	for line in arrivals:
   		if line.split()[0] == str(i) and line.split()[3] == 'P':
       			phasesP = []
       			phasesP.append(line.split()[2])
       			phasesP.append(line.split()[3])
       			arr_dic_P[line.split()[1]] = phasesP
   		elif line.split()[0] == str(i) and line.split()[3] == 'S':
       			phasesS = []
       			phasesS.append(line.split()[2])
       			phasesS.append(line.split()[3])
       			arr_dic_S[line.split()[1]] = phasesS
   		else:
       			continue
   	print starttime, type(starttime)
   	create_sfile(arr_dic_P,arr_dic_S,starttime)
	starttime += min
   	print i



    
    


