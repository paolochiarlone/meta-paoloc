#!/usr/bin/env python
import time

print("Read ADC on Grove connector no.1 and Blink LED on Grove connector no.2")

adcpath="/sys/bus/iio/devices/iio:device0/in_voltage0_raw"
gpiopath = "/sys/class/gpio/gpio508/value"

print("ADC: " + adcpath)
print("GPIO: " + gpiopath)
print

fw = open(gpiopath, 'w+')
fr = open(adcpath, 'r')

while (True):
  fr.seek(0)
  val = fr.read()
  print("Read=" + str(val))
  tout = float(val) / 2000.0
  # sys/class/gpio requires 0x0a31 ('1'+LF) for ON and 0x0a30 ('0'+LF) for OFF
  # remember bytes have to be inverted!!!!! (endianness)
  fw.write(b'\x31\x0a')
  fw.flush()
  time.sleep(tout)
  fw.write(b'\x30\x0a')
  fw.flush()
  time.sleep(tout)
  print("blink")

fw.close
