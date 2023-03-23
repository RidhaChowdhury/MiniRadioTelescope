# Radio Telescope

Main program for Penn State Harrisburg radio telescope project. 

Control hardware repository: https://github.com/drkntz/radiotelescope-PCB

Embedded firmware repository: https://github.com/drkntz/radiotelescope-firmware

This Python software is forked from UPENN project: https://github.com/UPennEoR/MiniRadioTelescope

## General structure of this repository

* The RTLSDR folder relates to the [rtl-sdr](rtl-sdr.com) module, which gets data from the antenna.

  * [RTLSDR/installing_pyrtlsdr:](RTLSDR/installing_pyrtlsdr) Instructions for installing pyrtlsdr, python lib for reading data.
  * [RTLSDR/rtlsdr_wrapper.py:](RTLSDR/rtlsdr_wrapper.py) Wrapper/basic example. Can get raw samples at a frequency and draw a plot.

* "earl" is the hostname of the laptop donated to serve as the control platform.
  * [earl/installing_earl:](earl/installing_earl) Instructions for installing arch on the laptop.

## Documentation
[Software documentation folder on Google Drive](https://drive.google.com/drive/folders/1lzj3X5Istw0j4d1xbYx2XgU6ZHmYsZLo)

* [Documentation for astropy_coordinates.py](https://docs.google.com/document/d/1qpQ_SRinI0ADAfMxYnLgn-8IxUDTiz-_WAb4TQxqFYk)

* [Documentation for RTLSDR/rtlsdr_wrapper.py](https://docs.google.com/document/d/1XA12joOU6Yji55qQAi5daokHakzWAKffufSam6EbvlQ)



