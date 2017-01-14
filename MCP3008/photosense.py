#!/usr/bin/python
# -*- coding: utf-8 -*-

""" this script reads the voltage over a 10k resistor
    that is connected in series with a photosensor to +3.3V
    then calculates the resistance of the photosensor
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
    
    R = 10000 * (3.3/V - 1)
    L = 30 / math.exp(math.log(R/10000)/0.7)

    print '{:.3f}'.format(V) + " V, " + '{:.0f}'.format(R) + " Ohm, " + '{:.1f}'.format(L)

    time.sleep(1)

except KeyboardInterrupt:
  print "end by user"

except ValueError:
  print "invalid value"

finally:
  spi.close()
  
# end
