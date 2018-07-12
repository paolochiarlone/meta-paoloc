# meta-paoloc

Digi Embedded paoloc meta-layer
===============================

This meta-layer is designed to create a pre-configured rootfs
with the necessary typical files used in a CC6UL project for
demos by the FAE.

Also it does change the DT files to configure the I/O correctly.

Specifically enables the GPIOs and ADC from *GPIO connector J30* and
uses the GPIOs available on *Video RGB PARALLEL J21*.

Lastly, it installs the standard .profile files for aliases on /home/root
as well as a series of bash scripts and Pythons scripts to work with
different I/Os, Expanders, etc.


Supported Platform
------------------
CC6UL SBC PRO
https://www.digi.com/products/embedded-systems/single-board-computers/connectcore-for-i-mx6ul-sbc-pro#productsupport


Requirements
------------
DEY 2.4r1


Version
-------
This is the first working release.


License
-------
Copyright 2018, Digi International Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
