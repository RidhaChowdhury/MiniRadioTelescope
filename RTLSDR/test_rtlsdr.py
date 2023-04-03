from pylab import *
from rtlsdr import *

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sdr.center_freq = 1.42e9
sdr.gain = 'auto'

# perform IQ correction
sdr.set_freq_correction(60)
sdr.set_iq_balance_mode(True)

samples = sdr.read_samples(256*1024)
sdr.close()

# calculate power from IQ samples
power = 10*np.log10(np.mean(np.abs(samples)**2))

# use matplotlib to estimate and plot the PSD
psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6) # expects frequency in MHz
xlabel('Frequency (MHz)')
ylabel('Relative power (dB)')

# display the calculated power
print(f"Power: {power:.2f} dBFS")

show()
