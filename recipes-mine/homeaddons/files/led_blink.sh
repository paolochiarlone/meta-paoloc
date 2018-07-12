gpiopath='/sys/class/gpio'

while true
do echo 1 > $gpiopath/gpio508/value
sleep 1
echo 0 > $gpiopath/gpio508/value
sleep 1
done
