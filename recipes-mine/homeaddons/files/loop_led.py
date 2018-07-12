#!/usr/bin/env python
import time

print("Blinking LED on Grove connector no.2 (Digital I/O)")

gpiopath = "/sys/class/gpio/gpio508/value"

f = open(gpiopath, 'w+')

while (True):
  # sys/class/gpio requires 0x0a31 ('1'+LF) for ON and 0x0a30 ('0'+LF) for OFF
  # remember bytes have to be inverted!!!!! (endianness)
  f.write(b'\x31\x0a')
  f.flush()
  time.sleep(0.3)
  f.write(b'\x30\x0a')
  f.flush()
  time.sleep(0.3)
  print("blink")

f.close
