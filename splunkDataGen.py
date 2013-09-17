#!/usr/bin/python

import datetime
import time
import random

#Seeds for user ids
fnSeed = ('james', 'john', 'michael', 'william', 'david', 'richard', 'charles', 'joseph', 'thomas', 'christopher', 'mary', 'patricia', 'linda', 'barbara', 'jennifer', 'maria', 'susan', 'margaret', 'dorothy', 'lisa')
lnSeed = ('smith', 'johnson', 'williams', 'brown', 'jones', 'davis', 'miller', 'wilson', 'moore', 'taylor', 'anderson', 'thomas', 'jackson', 'white', 'harris', 'martin', 'thompson', 'garcia', 'martinez')

#LDAP server config
ldapIP = '192.168.1.10'
ldapSvcName = 'LDAP'
ldapSvcMsg1 = 'Authentication: Failure Message: "Bad Password" for username='
ldapSvcMsg2 = 'Authentication: Failure Message: "Unable to connect to database" for username='

#WebApp server config
webappIP = '192.168.1.12'
webappSvcName = 'OIT Web App'
webappSvcMsg1 = 'Authentication: Failure Message: "Bad Password" for username= '
webappSvcMsg2 = 'Authentication: Failure Message: "Unable to connect to database" for username='
webappSvcMsg3 = 'Authentication: Success: username='

#SQL server config
sqlIP = '192.168.1.11'
sqlSvcName = 'SQL'
sqlSvcMsg1 = 'Message: "Running Backup Job"'
sqlSvcMsg2 = 'Message: "Queuing Database Requests"'
sqlSvcMsg3 = 'Message: "Unable To Process Requests From: 192.168.1.10"'

#Footprints server configurability
fpIP = '192.168.1.13'

#Change Management server config
cmIP = '192.168.1.14'

#Seeds for various time variables and offsets
today = datetime.datetime.now()
subWeeks = datetime.timedelta(days=90)#This sets how far back the data should go
weeksAgo = today - subWeeks  
addMinute = datetime.timedelta(minutes=1)
addSecond = datetime.timedelta(seconds=2)
addFiveMin = datetime.timedelta(minutes=5)


#Create the initial RFC entry
rfcOffset = weeksAgo - datetime.timedelta(minutes=5)
rfcComplete = rfcOffset.strftime('%m/%d/%Y %H:%M:%S')
print rfcComplete + ' ' + cmIP + ' RFC 301 Completed'

#Footprints ticket seed
fp = 1

while weeksAgo <= today:
    fname = random.choice(fnSeed)
    lname = random.choice(lnSeed)
    ct_weeksAgo = weeksAgo.strftime('%m/%d/%Y %H:%M:%S')  
    print ct_weeksAgo + ' ' + webappIP + ' ' + webappSvcName + ' ' + webappSvcMsg3 + '"' + fname + ' ' + lname + '"'
    weeksAgo = weeksAgo + addMinute + addSecond
    hour = weeksAgo.hour
    minute = weeksAgo.minute
    hrmin = '%02i' % hour + '%02i' % minute
    #Break to insert spike in log message for broken service
    if hrmin == '0800':
        print ct_weeksAgo + ' ' + sqlIP + ' ' + sqlSvcName + ' ' + sqlSvcMsg1
        print ct_weeksAgo + ' ' + sqlIP + ' ' + sqlSvcName + ' ' + sqlSvcMsg2
        for i in range(10):
            ct_weeksAgo = weeksAgo.strftime('%m/%d/%Y %H:%M:%S')
            print ct_weeksAgo + ' ' + webappIP + ' ' + webappSvcName + ' ' + webappSvcMsg2  + '"' + fname + ' ' + lname + '"'
            print ct_weeksAgo + ' ' + ldapIP + ' ' + ldapSvcName + ' ' + ldapSvcMsg2  + '"' + fname + ' ' + lname + '"'
            print ct_weeksAgo + ' ' + sqlIP + ' ' + sqlSvcName + ' ' + sqlSvcMsg3
            weeksAgo = weeksAgo + addSecond
        weeksAgo = weeksAgo + addSecond
        ct_weeksAgo = weeksAgo.strftime('%m/%d/%Y %H:%M:%S')
        print ct_weeksAgo + ' ' + sqlIP + ' service restarted'
        weeksAgo = weeksAgo + addMinute
        ct_weeksAgo = weeksAgo.strftime('%m/%d/%Y %H:%M:%S')
        print ct_weeksAgo + ' ' + fpIP + ' Footprints Issue: ' + (str(fp)).zfill(3) + ' Created for username=' + '"' + fname + ' ' + lname + '"' + ' ' + 'Description: Unable to login'
        fp = fp + 1   
    else:
        pass
    ranHr = random.randint(8, 16)
    ranMin = random.randint(10, 59)
    ranTime = '%02i' % ranHr + '%02i' % ranMin
    #Break to insert pseudo-random password reset events
    if hrmin == ranTime:
        fname = random.choice(fnSeed)
        lname = random.choice(lnSeed)
        print ct_weeksAgo + ' ' + ldapIP + ' ' + ldapSvcName + ' ' + ldapSvcMsg1  + '"' + fname + ' ' + lname + '"'
        weeksAgo = weeksAgo + addFiveMin
        ct_weeksAgo = weeksAgo.strftime('%m/%d/%Y %H:%M:%S')
        print ct_weeksAgo + ' ' + fpIP + ' Footprints Issue: ' + (str(fp)).zfill(3) + ' Created for username=' '"' + fname + ' ' + lname + '"' + ' ' + 'Description: Password reset'
        fp = fp + 1
    else:
        pass
        
        
        
        
