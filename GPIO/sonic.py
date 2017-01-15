#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import timeit
import math
import RPi.GPIO as GPIO

"""

"""

try:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT, initial=0)
    GPIO.setup(17, GPIO.IN)

    p = GPIO.PWM(4, 1)
    p.start(0.1)

    while True:

        # wait for start of echo
        GPIO.wait_for_edge(17, GPIO.RISING, timeout=2000)
        T1 = timeit.default_timer()

        #wait for end of echo
        GPIO.wait_for_edge(17, GPIO.FALLING, timeout=2000)
        T2 = timeit.default_timer()
        
        T = T2 - T1
        D = (T * 34300) / 2

        print "T: " + '{:7.3f}'.format(T*1000) + " ms, D: " + '{:.1f}'.format(D) + " cm"

except KeyboardInterrupt:
    
    print "end"

except Exception as e:

    print e

finally:

    p.stop()
    print "cleanup"
    GPIO.cleanup()
