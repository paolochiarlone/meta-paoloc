# Copyright (C) 2018 Digi International Inc.

FILESEXTRAPATHS_prepend := "${THISDIR}/${BPN}:"

SRC_URI_append_ccimx6ulsbc = " \
	file://0005-Final-modifications-for-ADC.patch \
	"

#file://0001-Enabling-GPIO-and-MCA-ADCs.patch
#file://0003-Changes-for-enabling-i.MX6UL-ADC2-ADC3-ADC5.patch
