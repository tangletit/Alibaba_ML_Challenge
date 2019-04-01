import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq

bearings = ['Bearing1_1', 'Bearing1_2', 'Bearing1_6', 'Bearing1_7']
names = ['hour', 'minute', 'second', 'micro', 'haccel', 'vaccel']

for bearing in bearings:
    os.chdir('Learning_set/' + bearing)
    i = 0
    haccel_means, vaccel_means, haccel_vars, vaccel_vars, haccel_kurts, vaccel_kurts, haccel_skews, vaccel_skews = [[] for _ in range(8)]
    for fname in glob.glob('*.csv'):
        # if i % 10 != 0:
        #     i += 1
        #     continue
        df = pd.read_csv(fname, names=names)
        haccel_means.append(df['haccel'].mean())
        vaccel_means.append(df['vaccel'].mean())
        haccel_vars.append(df['haccel'].var())
        vaccel_vars.append(df['vaccel'].var())
        haccel_kurts.append(df['haccel'].kurt())
        vaccel_kurts.append(df['vaccel'].kurt())
        haccel_skews.append(df['haccel'].skew())
        vaccel_skews.append(df['vaccel'].skew())
        i += 1

    times = [10*_ for _ in range(len(haccel_means))]

    df = pd.DataFrame({'time': times,
                       'haccel_mean': haccel_means,
                       'vaccel_mean': vaccel_means,
                       'haccel_var': haccel_vars,
                       'vaccel_var': vaccel_vars,
                       'haccel_kurt': haccel_kurts,
                       'vaccel_kurt': vaccel_kurts,
                       'haccel_skew': haccel_skews,
                       'vaccel_skew': vaccel_skews})

    os.chdir('../..')  # save csv to project directory
    df.to_csv(bearing + '_time_domain.csv', index=False)

# ax = plt.subplot(241)
# plt.plot(times, haccel_means)
# ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Mean')
# ax = plt.subplot(242)
# plt.plot(times, vaccel_means)
# ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Mean')
# ax = plt.subplot(243)
# plt.plot(times, haccel_vars)
# ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Variance')
# ax = plt.subplot(244)
# plt.plot(times, vaccel_vars)
# ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Variance')
# ax = plt.subplot(245)
# plt.plot(times, haccel_kurts)
# ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Kurtosis')
# ax = plt.subplot(246)
# plt.plot(times, vaccel_kurts)
# ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Kurtosis')
# ax = plt.subplot(247)
# plt.plot(times, haccel_skews)
# ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Skewness')
# ax = plt.subplot(248)
# plt.plot(times, vaccel_skews)
# ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Skewness')
#
# plt.tight_layout()
# plt.show()
