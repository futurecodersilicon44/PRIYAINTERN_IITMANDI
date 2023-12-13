# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:23:34 2023

@author: jaipr
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_signal_and_fourier(file_path, sampling_rate):
    # Read earthquake amplitudes from the text file
    amplitudes = np.loadtxt(file_path)

    # Assuming a constant time spacing based on the sampling rate
    time = np.arange(0, len(amplitudes)) / sampling_rate

    # Plot the earthquake signal
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(time, amplitudes)
    plt.title('Earthquake Signal')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude(micrometer)')

    # Compute and plot the Fourier Transform
    fourier_transform = np.fft.fft(amplitudes)
    frequencies = np.fft.fftfreq(len(time), 1/sampling_rate)

    plt.subplot(2, 1, 2)
    plt.plot(np.abs(frequencies), np.abs(fourier_transform))
    plt.title('Fourier Transform')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude(micromete)')
    plt.tight_layout()
    plt.show()

# Specify the path to your earthquake amplitudes text file
file_path = "x1.txt"

# Specify the assumed sampling rate (replace with the actual value if known)
sampling_rate = 1/0.005

# Call the function to plot the signal and Fourier Transform
plot_signal_and_fourier(file_path, sampling_rate)
