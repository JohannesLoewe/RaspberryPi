#!/usr/bin/python
# -*- coding: utf-8 -*-

""" this script reads the voltage over a 10k resistor
    that is connected in series with a thermistor to +3.3V
    then calculates the resistance of the thermistor and
    converts it to the temperature
"""

import spidev
import time
import math

spi = spidev.SpiDev()
spi.open(0,0)

try:
  while True:
    rcv = spi.xfer2([1, 8 << 4, 0])
    val = (rcv[1] & 3) * 256 + rcv[2]
    V   = val / 1024.0 * 3.3

    if val == 0 :
      raise ValueError('zero voltage reading')
    
    Rt = 10000 * (3.3/V - 1)
    T  = 1.0/(1.0/298.15 + math.log(Rt/10000)/4050.0) - 273.15

    print '{:.3f}'.format(V) + " V, " + '{:.0f}'.format(Rt) + " mA, " + '{:.1f}'.format(T) + " °C"

    time.sleep(1)

except KeyboardInterrupt:
  print "end by user"

except ValueError:
  print "invalid value"

finally:
  spi.close()
  
# end
