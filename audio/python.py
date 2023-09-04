# load and plot audio in python

# import packages
from scipy.io import wavfile # for reading .WAV audio
import numpy as np # HUGE speedup using numpy/scipy compared to base python
import matplotlib.pyplot as plt # plotting


def plot_fft_first_second(fname: str) -> None:
    rate, data = wavfile.read(fname)
    # slice first second
    first_second = data[:rate - 1]
    # absolute of dft of first second
    abs_fft = np.abs(np.fft.fft(first_second))
    # plot
    plt.plot(abs_fft)
    # save as first
    plt.savefig("plot.pdf")
    return


plot_fft_first_second("my_file.wav")
