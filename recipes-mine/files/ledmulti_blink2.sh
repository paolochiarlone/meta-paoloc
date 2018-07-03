#!/bin/sh

gpiopath='/sys/class/gpio'
leda=gpio69
ledb=gpio71
ledc=gpio73
ledd=gpio75
lede=gpio77
stime=0.2

while true
do echo 1 > $gpiopath/$leda/value
sleep $stime
echo 1 > $gpiopath/$ledb/value
sleep $stime
echo 1 > $gpiopath/$ledc/value
sleep $stime
echo 1 > $gpiopath/$ledd/value
sleep $stime
echo 1 > $gpiopath/$lede/value
sleep $stime
echo 0 > $gpiopath/$leda/value
sleep $stime
echo 0 > $gpiopath/$ledb/value
sleep $stime
echo 0 > $gpiopath/$ledc/value
sleep $stime
echo 0 > $gpiopath/$ledd/value
sleep $stime
echo 0 > $gpiopath/$lede/value
sleep $stime
done
