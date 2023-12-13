# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 10:51:59 2023

@author: jaipr
"""

# -*- coding: utf-8 -*-


import os
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
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (cm/s^2)')

    # Compute and plot the Fourier Transform
    fourier_transform = np.fft.fft(amplitudes)
    frequencies = np.fft.fftfreq(len(time), 1/sampling_rate)

    plt.subplot(2, 1, 2)
    plt.plot(np.abs(frequencies), np.abs(fourier_transform))
    plt.title('Fourier Transform')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (cm/s^2)')
    plt.tight_layout()
    plt.show()

def process_files_in_directory(directory_path, sampling_rate):
    # Loop over all files in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            
            # Call the function to plot the signal and Fourier Transform for each file
            plot_signal_and_fourier(file_path, sampling_rate)

# Specify the directory containing the .txt files
directory_path = "C:/Users/jaipr/OneDrive/Desktop/task2/directory"

# Specify the assumed sampling rate (replace with the actual value if known)
sampling_rate = 1/0.005

# Call the function to process all .txt files in the directory
process_files_in_directory(directory_path, sampling_rate)