#!/usr/bin/env python
#
# Usage:
# CC6UL SBC with PCF8574 Multiplexer connected on I2C1
# (pin 33, 34 of RGB connector)
#

import time
import sys
from subprocess import call

CMD = "i2cset"
# I2C-0
BUS = "%d" % 0
# address on bus is 0x38
ADDR = "0x%0.2X" % 0x38

DELAY = 0.100
DELAYLONG = (DELAY * 2)
DELAYSHORT = 0.040

test = call(["which", CMD])
if (test == 1):
  sys.exit("\nERROR: ic2set not found!\n")

print("\nUsing I2C1 connected to PCF8574 Mux, toggle I/Os in loop\n")

while (True):
  # loop for 5 bit as I only have 5 LED :(
  for l in range(0, 32):
    ###a = call(["i2cset", "0", "0x38", "0", "0x00", "-y"])
    a = call([CMD, BUS, ADDR, "0", "0x%0.2X" % l, "-y"])
    time.sleep(DELAY)

  for l in range(0, 6):
    a = call([CMD, BUS, ADDR, "0", "0x1F", "-y"])
    time.sleep(DELAY * (l + 1))
    a = call([CMD, BUS, ADDR, "0", "0x00", "-y"])
    time.sleep(DELAYLONG)

  for j in range(0, 4):
    for l in [1, 2, 4, 8, 16]:
      a = call([CMD, BUS, ADDR, "0", "0x%0.2X" % l, "-y"])
      time.sleep(DELAYSHORT)

    for l in [16, 8, 4, 2, 1]:
      a = call([CMD, BUS, ADDR, "0", "0x%0.2X" % l, "-y"])
      time.sleep(DELAYSHORT)

print("done!\n")