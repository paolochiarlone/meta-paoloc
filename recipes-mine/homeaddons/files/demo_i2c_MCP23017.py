#!/usr/bin/env python
#
# Usage:
# CC6UL SBC with MCP23017 Multiplexer connected on I2C1
# (pin 33, 34 of RGB connector)
#

import time
import sys
from subprocess import call

CMD = "i2cset"
# I2C-0
BUS = "%d" % 0
# address on bus is 0x20
ADDR = "0x%0.2X" % 0x20

# i2cset -y 0 0x20 0x12 0x05
# i2cset -y 0 0x20 0x12 0x12
# i2cset -y 0 0x20 0x12 0x05

DELAY = 0.050

test = call(["which", CMD])
if (test == 1):
  sys.exit("\nERROR: ic2set not found!\n")

print("\nSimple loop for LED\n")

# this is the reset for PortA and PortB
a = call([CMD, BUS, ADDR, "0", "0", "-y"])
a = call([CMD, BUS, ADDR, "1", "0", "-y"])

while (True):
  # loop for 5 bit as I only have 5 LED :(
  
  for l in range(0, 32):
      # address 0x12 is PortA, address 0x13 is PortB
      a = call([CMD, BUS, ADDR, "0x12", "0x%0.2X" % l, "-y"])
      time.sleep(DELAY)

  for l in range(31, -1, -1):
      # address 0x12 is PortA, address 0x13 is PortB
      a = call([CMD, BUS, ADDR, "0x12", "0x%0.2X" % l, "-y"])
      time.sleep(DELAY)

print("done!\n")

