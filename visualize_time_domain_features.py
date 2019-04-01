import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np

bearings = ['Bearing1_1', 'Bearing1_2', 'Bearing1_6', 'Bearing1_7']
plot_num = 1
for bearing in bearings:
    df = pd.read_csv(bearing + '_time_domain_features.csv')
    times = df['time']
    plt.figure(plot_num)
    ax = plt.subplot(241)
    plt.plot(times, df['haccel_mean'])
    ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Mean')

    ax = plt.subplot(242)
    plt.plot(times, df['vaccel_mean'])
    ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Mean')

    ax = plt.subplot(243)
    plt.plot(times, df['haccel_var'])
    ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Variance')

    ax = plt.subplot(244)
    plt.plot(times, df['vaccel_var'])
    ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Variance')

    ax = plt.subplot(245)
    plt.plot(times, df['haccel_kurt'])
    ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Kurtosis')

    ax = plt.subplot(246)
    plt.plot(times, df['vaccel_kurt'])
    ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Kurtosis')

    ax = plt.subplot(247)
    plt.plot(times, df['haccel_skew'])
    ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Skewness')

    ax = plt.subplot(248)
    plt.plot(times, df['vaccel_skew'])
    ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Skewness')

    plt.tight_layout()
    plt.savefig(bearing + '_time_domain_features.png')
    plot_num += 1

plt.show()
