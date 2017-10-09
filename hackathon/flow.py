import RPi.GPIO as GPIO
import time, sys
import mcp3008
from random import randint
FLOW_SENSOR = 22
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)

global count
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
TRIG = 21                     
ECHO = 20 

GPIO.setup(TRIG,GPIO.OUT)             
GPIO.setup(ECHO,GPIO.IN)

url="http://virusattack.pythonanywhere.com/get"
def countPulse(channel):
   global count
   if start_counter == 1:
      count = count+1
      #print count
      flow = count / (60 * 7.5)
      #print(flow)

GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)

while True:
    try:
        start_counter = 1
        time.sleep(1)
        start_counter = 0
        flow = (count * 60 * 2.25 / 1000)
        print "The flow is: %.3f Liter/min" % (flow)
        count = 0
        time.sleep(1)

    except KeyboardInterrupt:
        print '\ncaught keyboard interrupt!, bye'
        GPIO.cleanup()
        sys.exit()
    p = mcp3008.readadc(1)
    print p
    s = "water leakage is detected"
    if p > 800 :
        print "pure"
        GPIO.output(TRIG, False)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)               
        GPIO.output(TRIG, False)  
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()        
        while GPIO.input(ECHO)==1:            
            pulse_end = time.time()  
        pulse_duration = pulse_end - pulse_start
                     
        distance = pulse_duration * 17150        
        distance = round(distance, 2)
        #distance = 30-distance
        print distance
        #Time =datetime.datetime.now()
        m = mcp3008.readadc(0)
        s=""
        print m
        if distance<10 :
           if m==0 :
              GPIO.output(26, True)
              time.sleep(3)
              GPIO.output(26,False)
              s="supplying water to drinking water tank"
           else :
              s="the pipe may be damaged in drinking water supply"
        else :
           GPIO.output(26,False)

        #turbidity
        data = {'result':s ,'waterlevel':distance,'waterflow':flow,'turbidity':p,'ph':randint(0, 9),'soilmoisture':m}    
        #print m
        requests.get(url,params=data)
        #print p
    else :
        print "impure"
        GPIO.output(TRIG, False)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)               
        GPIO.output(TRIG, False)  
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()        
        while GPIO.input(ECHO)==1:            
            pulse_end = time.time()  
        pulse_duration = pulse_end - pulse_start
                     
        distance = pulse_duration * 17150        
        distance = round(distance, 2)
        #distance = 30-distance
        print distance
        #Time =datetime.datetime.now()
        m = mcp3008.readadc(0)
        s=""
        print m
        if distance<10 :
           if m==0 :
              GPIO.output(2, True)
              time.sleep(3)
              GPIO.output(2,False)
              s="supplying water to daily usage water tank"
           else :
              s="the pipe may be damaged in daily usage water supply"
        else :
           GPIO.output(2,False)

        #turbidity
        data = {'result':s ,'waterlevel':distance,'waterflow':flow,'turbidity':p,'ph':randint(0, 9),'soilmoisture':m}    
        #print m
        requests.get(url,params=data)
        
    time.sleep(1)
