# Copyright (C) 2018 Digi International Inc.

SUMMARY = "Home Addons"
DESCRIPTION = "Adding optional files to homedir"

LICENSE = "CLOSED"
###BB_STRICT_CHECKSUM = "0"

FILESEXTRAPATHS_prepend := "${THISDIR}/files:"

# Specify where to get the files
S = "${WORKDIR}"

inherit allarch

###ALLOW_EMPTY_${PN} = "1"

RPROVIDES_${PN} += "${PN}"

SRC_URI = " \
	file://LED_kitt.py \
	"
###	file://demo_i2c_MCP23017.py
###	file://demo_i2c_PCF8574.py
###	file://gpio67_button.sh
###	file://gpio75_led_on_off.sh
###	file://LED_kitt.py
###	file://ledmulti2.sh
###	file://ledmulti_blink2.sh
###	file://ledmulti_blink.sh
###	file://setup_demo_gpio.sh
###	file://setup_gpioled.sh
###	file://timer_adc_led.sh

do_install_append() {
	# creating the destination directories
	install -d ${D}/home
	install -d ${D}/home/root

	# extra files need to go in the respective directories
	install -m 0755 ${WORKDIR}/LED_kitt.py ${D}/home/root/
	###install -m 0644 ${MY_FILES}/.profile ${D}/home/root/
	###install -m 0644 ${MY_FILES}/setup_gpioled.sh ${D}/home/root
}

###INSANE_SKIP_${PN} += "installed-vs-shipped"
PACKAGES =+ "${PN}"
FILES_${PN} += "/home/* /home/root/* "

