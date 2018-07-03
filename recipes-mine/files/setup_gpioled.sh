#!/bin/sh

gpiopath='/sys/class/gpio'
leda=69
ledb=71
ledc=73
ledd=75
lede=77

cd /sys/class/gpio/

echo $leda > export
echo $ledb > export
echo $ledc > export
echo $ledd > export
echo $lede > export

echo out > gpio$leda/direction
echo out > gpio$ledb/direction
echo out > gpio$ledc/direction
echo out > gpio$ledd/direction
echo out > gpio$lede/direction
