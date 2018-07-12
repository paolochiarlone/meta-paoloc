# Copyright (C) 2018 Digi International Inc.

SUMMARY = "Home Addons"
DESCRIPTION = "Adding optional files to homedir"
LICENSE = "CLOSED"

FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

RPROVIDES_${PN} += "${PN}"


SRC_URI = " \
	file://.profile \
	file://LED_kitt.py \
	file://demo_i2c_MCP23017.py \
	file://demo_i2c_PCF8574.py \
	file://gpio67_button.sh \
	file://gpio75_led_on_off.sh \
	file://ledmulti2.sh \
	file://ledmulti_blink2.sh \
	file://ledmulti_blink.sh \
	file://setup_demo_gpio.sh \
	file://setup_gpioled.sh \
	file://timer_adc_led.sh \
"

# Specify where to get the files
S = "${WORKDIR}"

do_configure[noexec] = "1"
do_compile[noexec] = "1"

do_install() {
	# creating the destination directories
	install -d ${D}/home/root

	# extra files need to go in the respective directories
	install -m 0644 ${WORKDIR}/.profile ${D}/home/root/
	install -m 0644 ${WORKDIR}/LED_kitt.py ${D}/home/root/
	install -m 0644 ${WORKDIR}/demo_i2c_MCP23017.py ${D}/home/root
	install -m 0644 ${WORKDIR}/demo_i2c_PCF8574.py ${D}/home/root
	install -m 0755 ${WORKDIR}/gpio67_button.sh ${D}/home/root
	install -m 0755 ${WORKDIR}/gpio75_led_on_off.sh ${D}/home/root
	install -m 0755 ${WORKDIR}/ledmulti2.sh ${D}/home/root
	install -m 0755 ${WORKDIR}/ledmulti_blink2.sh ${D}/home/root
	install -m 0755 ${WORKDIR}/ledmulti_blink.sh ${D}/home/root
	install -m 0755 ${WORKDIR}/setup_demo_gpio.sh ${D}/home/root
	install -m 0755 ${WORKDIR}/setup_gpioled.sh ${D}/home/root
	install -m 0755 ${WORKDIR}/timer_adc_led.sh ${D}/home/root
}

FILES_${PN} += "/home/root/* /home/root/.profile "

