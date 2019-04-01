import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq
from scipy import signal

bearings = ['Bearing1_1', 'Bearing1_2', 'Bearing1_6', 'Bearing1_7']
names = ['hour', 'minute', 'second', 'micro', 'haccel', 'vaccel']
num_points = 2560

for bearing in bearings:
    os.chdir('Learning_set/' + bearing)
    i = 0
    haccel_trapz_int1, haccel_trapz_int2 = [], []
    vaccel_trapz_int1, vaccel_trapz_int2 = [], []
    haccel_peak_int3, haccel_peak_int4 = [], []
    vaccel_peak_int3, vaccel_peak_int4 = [], []

    plot_num = 1
    for fname in glob.glob('*.csv'):
        # if i % 100 != 0:
        #     i += 1
        #     continue
        df = pd.read_csv(fname, names=names)
        freqs = fftfreq(num_points)
        mask = freqs > 0
        freqs_mask = freqs[mask]

        haccel_vals = 2.0*np.abs(fft(df['haccel'])/num_points)
        vaccel_vals = 2.0*np.abs(fft(df['vaccel'])/num_points)
        haccel_vals_total = sum(haccel_vals)
        vaccel_vals_total = sum(vaccel_vals)
        haccel_vals = haccel_vals/haccel_vals_total
        vaccel_vals = vaccel_vals/vaccel_vals_total

        haccel_vals_mask = haccel_vals[mask]
        vaccel_vals_mask = vaccel_vals[mask]

        nperseg = 250
        freqs_welch, haccel_vals_welch = signal.welch(df['haccel'], window='hamming', nperseg=nperseg, noverlap=0)
        freqs_welch, vaccel_vals_welch = signal.welch(df['vaccel'], window='hamming', nperseg=nperseg, noverlap=0)

        # plt.figure(plot_num)
        # plt.plot(freqs_mask, haccel_vals_mask)
        # plt.plot(freqs_mask, vaccel_vals_mask)
        # plt.plot(freqs_welch, haccel_vals_welch)
        # plt.plot(freqs_welch, vaccel_vals_welch)

        # horiz. accel. freq. intervals of interest (for trapz)
        haccel_int1 = [0.1, 0.18]
        haccel_int2 = [0.4, 0.5]
        # horiz. accel. freq. intervals of interest (for peak)
        haccel_int3 = [0.071, 0.18]
        haccel_int4 = [0.35, 0.42]

        # indices of horiz. accel. freq. intervals of interest
        haccel_inds1 = [(np.abs(freqs_mask-freq)).argmin() for freq in haccel_int1]
        haccel_inds2 = [(np.abs(freqs_mask - freq)).argmin() for freq in haccel_int2]
        haccel_inds3 = [(np.abs(freqs_welch-freq)).argmin() for freq in haccel_int3]
        haccel_inds4 = [(np.abs(freqs_welch-freq)).argmin() for freq in haccel_int4]

        # vert. accel. freq. intervals of interest (for trapz)
        vaccel_int1 = [0.185, 0.24]
        vaccel_int2 = [0.36, 0.475]
        # vert. accel. freq. intervals of interest (for peak)
        vaccel_int3 = vaccel_int1
        vaccel_int4 = vaccel_int2

        # indices of vert. accel. freq. intervals of interest
        vaccel_inds1 = [(np.abs(freqs_mask-freq)).argmin() for freq in vaccel_int1]
        vaccel_inds2 = [(np.abs(freqs_mask - freq)).argmin() for freq in vaccel_int2]
        vaccel_inds3 = [(np.abs(freqs_welch-freq)).argmin() for freq in vaccel_int3]
        vaccel_inds4 = [(np.abs(freqs_welch-freq)).argmin() for freq in vaccel_int4]

        haccel_trapz_int1.append(np.trapz(haccel_vals_mask[haccel_inds1[0]:haccel_inds1[1]], x=freqs_mask[haccel_inds1[0]:haccel_inds1[1]]))
        haccel_trapz_int2.append(np.trapz(haccel_vals_mask[haccel_inds2[0]:haccel_inds2[1]], x=freqs_mask[haccel_inds2[0]:haccel_inds2[1]]))
        haccel_peak_int3.append(freqs_welch[haccel_inds3[0] + (haccel_vals_welch[haccel_inds3[0]:haccel_inds3[1]]).argmax()])
        haccel_peak_int4.append(freqs_welch[haccel_inds4[0] + (haccel_vals_welch[haccel_inds4[0]:haccel_inds4[1]]).argmax()])

        vaccel_trapz_int1.append(np.trapz(vaccel_vals_mask[vaccel_inds1[0]:vaccel_inds1[1]], x=freqs_mask[vaccel_inds1[0]:vaccel_inds1[1]]))
        vaccel_trapz_int2.append(np.trapz(vaccel_vals_mask[vaccel_inds2[0]:vaccel_inds2[1]], x=freqs_mask[vaccel_inds2[0]:vaccel_inds2[1]]))
        vaccel_peak_int3.append(freqs_welch[vaccel_inds3[0] + (vaccel_vals_welch[vaccel_inds3[0]:vaccel_inds3[1]]).argmax()])
        vaccel_peak_int4.append(freqs_welch[vaccel_inds4[0] + (vaccel_vals_welch[vaccel_inds4[0]:vaccel_inds4[1]]).argmax()])

        # plot_num += 1
        i += 1

    times = [10*_ for _ in range(len(haccel_trapz_int1))]

    df = pd.DataFrame({'time': times,
                       'haccel_trapz_int1': haccel_trapz_int1,
                       'haccel_trapz_int2': haccel_trapz_int2,
                       'haccel_peak_int3': haccel_peak_int3,
                       'haccel_peak_int4': haccel_peak_int4,
                       'vaccel_trapz_int1': vaccel_trapz_int1,
                       'vaccel_trapz_int2': vaccel_trapz_int2,
                       'vaccel_peak_int3': vaccel_peak_int3,
                       'vaccel_peak_int4': vaccel_peak_int4})

    os.chdir('../..')  # save csv to project directory
    df.to_csv(bearing + '_freq_domain_features.csv', index=False)

# plt.show()
