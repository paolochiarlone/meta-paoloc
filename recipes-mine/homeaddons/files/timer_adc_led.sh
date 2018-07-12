adcpath='/sys/bus/iio/devices/iio:device0'
gpiopath='/sys/class/gpio'

while true
do cat $adcpath/in_voltage0_raw
val=`cat $adcpath/in_voltage0_raw`
tout=$(expr $val / 1000)
echo $tout
echo 1 > $gpiopath/gpio508/value
sleep $tout
echo 0 > $gpiopath/gpio508/value
sleep $tout
done