#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

try:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(4, GPIO.OUT, initial=0)

    while GPIO.input(17) :
        pass

    print "starting low"

    while True:
        GPIO.output(4, 1)
        print "loading"

        while not GPIO.input(17) :
            pass

        print "now high"
        time.sleep(2)
        
        GPIO.output(4, 0)

        print "discharging"

        while GPIO.input(17) :
            pass

        print "now low"
        time.sleep(2)

except:
    
    print "end"
    
finally:

    GPIO.cleanup()
