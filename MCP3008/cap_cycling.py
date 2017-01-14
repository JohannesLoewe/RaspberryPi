#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import timeit
import math
import RPi.GPIO as GPIO

"""
100 uF
33.0 kOhm = 2.007604 s : 16.437 kOhm/s
19.6 kOhm = 1.214000 s : 16.145 kOhm/s
10.0 kOhm = 0.615496 s : 16.247 kOhm/s
average                  16.276 kOhm/s

10 uF average = 15.87 kOhm/s
"""

def RCTime():

    T1 = timeit.default_timer()

    GPIO.output(4, 1)
    GPIO.wait_for_edge(17, GPIO.RISING, bouncetime=10, timeout=1000)

    GPIO.output(4, 0)
    GPIO.wait_for_edge(17, GPIO.FALLING, bouncetime=10, timeout=1000)

    return timeit.default_timer() - T1

try:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(4, GPIO.OUT, initial=0)

    time.sleep(2)

    while True:

        T    = RCTime()
        Rt   = T * 158800 - 10000
        Temp = 1.0/(1.0/298.15 + math.log(Rt/10000)/4050.0) - 273.15

        print "RCTime: " + '{:.3f}'.format(T) + ", Rt: " + '{:.0f}'.format(Rt) + ", Temp: " + '{:.1f}'.format(Temp)

        time.sleep(2)


except KeyboardInterrupt:
    
    print "end"

except Exception as e:

    print e

finally:

    print "cleanup"
    GPIO.cleanup()
