# meta-paoloc

Digi Embedded PaoloC layer
==========================

This meta-layer is designed to create a pre-configured rootfs
with the necessary typical files used in a CC6UL project for
demos by the FAE.

Also it does change the DT files to configure the I/O correctly.

Specifically enables the GPIOs and ADC from GPIO connector J30 and
uses the GPIOs available on J21 Video RGB PARALLEL.

Lastly, it installs the standard .profile files for aliases on /home/root
as well as a series of bash scripts and Pythons scripts to work with
different I/Os, Expanders, etc.

Supported Platform
------------------
CC6UL SBC PRO

Requirements
------------
DEY 2.4r1

Version
-------
This is the first working release.

