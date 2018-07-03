#!/bin/sh
gpiopath='/sys/class/gpio'

echo 75 > $gpiopath/export
echo out > $gpiopath/gpio75/direction

echo "Turning the LED ON"
echo 1 > $gpiopath/gpio75/value

sleep 5

echo "Turning the LED OFF"
echo 0 > $gpiopath/gpio75/value