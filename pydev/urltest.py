#!/usr/bin/env python
# -*- coding: utf8 -*-

import threading
import time
import httplib



HOST = "192.168.123.99";
PORT = 80;
URL = "/?123" #家参数防止缓存

TOTAL = 0 #总数
SUCC = 0 #相应成功数
FAIL = 0
EXCEPT = 0
MAXTIME = 0
MINTIME = 100
GT3 = 0
LT3 = 0

class RequestThread(threading.Thread):
    def __init__(self, thread_name):
        threading.Thread.__init__(self)
        self.test_count = 0
    def run(self):
        self.test_performace()
    def test_performace(self):
        global TOTAL
        global SUCC
        global FAIL
        global EXCEPT
        global GT3
        global LT3
        try:
            st = time.time()
            conn = httplib.HTTPConnection(HOST,PORT,False)
            conn.request('GET',URL)
            res = conn.getresponse()
            start_time
            if res.status == 200:
                TOTAL+=1
                SUCC+=1
            else:
                TOTAL+=1
                FAIL+=1
            time_span = time.time()-st 
            print '%s:%f\n'%(self.name,time_span)
            if time_span>3:
                GT3+=1
            else:
                LT3+=1
        except Exception,e:
                print e
                TOTAL+=1
                EXCEPT+=1
        conn.close()
    def maxtime(self,ts):
        global MAXTIME
        print ts
        if ts>MAXTIME:
            MAXTIME=ts
    def mintime(self,ts):
        global MINTIME
        if ts<MINTIME:
            MINTIME=ts


print '===============task start==============='

start_time = time.time()

thread_count = 100
 
i = 0  
while i <= thread_count:  
    t = RequestThread("thread" + str(i))  
    t.start()  
    i += 1  
t=0
while TOTAL<thread_count|t>50:  
        print "total:%d,succ:%d,fail:%d,except:%d\n"%(TOTAL,SUCC,FAIL,EXCEPT)  
        print HOST,URL  
        t+=1  
        time.sleep(1)  
print '===========task end==========='  
print "total:%d,succ:%d,fail:%d,except:%d"%(TOTAL,SUCC,FAIL,EXCEPT)  
print 'response maxtime:',MAXTIME  
print 'response mintime',MINTIME  
print 'great than 3 seconds:%d,percent:%0.2f'%(GT3,float(GT3)/TOTAL)  
print 'less than 3 seconds:%d,percent:%0.2f'%(LT3,float(LT3)/TOTAL)

        
        
        
        
        
        
        
        
        
        
        