#!/usr/bin/env python
#
# Usage:
# CC6UL SBC with PCF8574 Multiplexer connected on I2C1 (pin 33, 34 of RGB connector)
#

import time
import sys
from subprocess import call

CMD = "i2cset"
# I2C-0
BUS = "%d" % 0
# address on bus is 0x38
ADDR = "0x%0.2X" % 0x38

DELAYSHORT = 0.060
DELAYMIN = 0.005

test = call(["which", CMD])
if (test == 1):
  sys.exit("\nERROR: ic2set not found!\n")

print("\nSupercar Kitt LED\n")

while (True):

    j = 0
    for l in [1, 3, 2, 6, 4, 12, 8, 24, 16]:
      a = call([CMD, BUS, ADDR, "0", "0x%0.2X" % l, "-y"])
      if (j == 0):
          time.sleep(DELAYSHORT)
          j = 1
      else:
          time.sleep(DELAYMIN)
          j = 0

    j = 0
    for l in [16, 24, 8, 12, 4, 6, 2, 3, 1]:
      a = call([CMD, BUS, ADDR, "0", "0x%0.2X" % l, "-y"])
      if (j == 0):
          time.sleep(DELAYSHORT)
          j = 1
      else:
          time.sleep(DELAYMIN)
          j = 0

print("done!\n")