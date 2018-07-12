#!/bin/sh

gpiopath='/sys/class/gpio'
ticks=100
 
echo 67 > $gpiopath/export
echo in > $gpiopath/gpio67/direction

echo "Press the User Button before 10 seconds"
until [ `cat $gpiopath/gpio67/value` -eq "0" ] || [ $ticks -eq 0 ];
do
        sleep 0.1
        ticks=$((ticks-1))
done
 
if [ $ticks -eq 0 ]; then
        printf "Timed out\n"
else
        printf "Button pressed\n"
fi