#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:55:36 2017

@author: jaguirre
Modified by mpeschel10
"""

#TODO: implement something to deal with the center frequency spike.
#      display a bunch of samples with locations as a heatmap.
#      integrate with astropy somehow for storing the samples with their sample_locations.

HYDROGEN_FREQUENCY = 1420405751.768
RTLSDR_SAMPLE_LENGTH = 256
RTLSDR_MAX_RATE = 3.2e6

import math

import logging
logger = logging.getLogger(__name__)
fh = logging.StreamHandler()
fh.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logger.addHandler(fh)

import rtlsdr

global_sdr = None
def open_global_sdr():
    global global_sdr
    if not global_sdr is None:
        return
    import atexit
    atexit.register(close_global_sdr)
    logger.debug('Opening global, persistent RTLSDR connection.')
    logger.debug('If the global connection interferes with your other rtlsdr.RtlSdr() calls,')
    logger.debug(' either call get_samples() with use_global_sdr=False,')
    logger.debug(' or reuse rtlsdr_wrapper.global_sdr instead of opening new ones.')
    global_sdr = rtlsdr.RtlSdr()

def close_global_sdr():
    global global_sdr
    logger.debug('Closing global, persistent RTLSDR connection.')
    global_sdr.close()

def get_samples(frequency, rate=1e6, count=RTLSDR_SAMPLE_LENGTH*1024, time=None, use_global_sdr=True):
    global global_sdr
    if not time is None:
        count = math.ceil(time * rate / 256) * 256
    elif count % RTLSDR_SAMPLE_LENGTH != 0:
        raise Exception('Sample count for rtlsdr MUST be a multiple of {} for some reason.'.format(RTLSDR_SAMPLE_LENGTH))
    
    if use_global_sdr:
        if global_sdr is None:
            open_global_sdr()
        sdr = global_sdr
    else:
        logger.debug('Opening RTLSDR connection.')
        sdr = rtlsdr.RtlSdr()

    sdr.sample_rate = rate
    sdr.center_freq = frequency
    sdr.gain = 'auto'

    samples = sdr.read_samples(count)
    
    if not use_global_sdr:
        logger.debug('Closing RTLSDR connection.')
        sdr.close()
    
    return samples

def plot(frequency, rate=1e6, count=None, time=1, show=True, use_global_sdr=True):
    import matplotlib.pyplot as plt
    samples = get_samples(frequency, rate, count, time, use_global_sdr)
    sample_count = round(len(samples) / RTLSDR_SAMPLE_LENGTH)
    next_power_of_two = 2 ** math.ceil(math.log(sample_count, 2))
    
    plt.figure()
    plt.clf()
    
    plt.psd(samples, NFFT=next_power_of_two, Fs=rate, Fc=frequency)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Relative power (dB)')

    if show:
        plt.show()


def main():
    # logger.setLevel(logging.DEBUG)
    frequency = HYDROGEN_FREQUENCY
    rate = RTLSDR_MAX_RATE
    plot(frequency, rate)

if __name__ == '__main__':
    main()
