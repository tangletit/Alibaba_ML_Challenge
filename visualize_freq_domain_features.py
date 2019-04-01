import pandas as pd
import matplotlib.pyplot as plt

bearings = ['Bearing1_1', 'Bearing1_2', 'Bearing1_6', 'Bearing1_7']
plot_num = 1
for bearing in bearings:
    df = pd.read_csv(bearing + '_freq_domain_features.csv')
    times = df['time']
    plt.figure(plot_num)
    ax = plt.subplot(241)
    plt.plot(times, df['haccel_trapz_int1'])
    ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('FFT Interval 1 Integral')

    ax = plt.subplot(242)
    plt.plot(times, df['vaccel_trapz_int1'])
    ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('FFT Interval 1 Integral')

    ax = plt.subplot(243)
    plt.plot(times, df['haccel_trapz_int2'])
    ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('FFT Interval 2 Integral')

    ax = plt.subplot(244)
    plt.plot(times, df['vaccel_trapz_int2'])
    ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('FFT Interval 2 Integral')

    ax = plt.subplot(245)
    plt.plot(times, df['haccel_peak_int3'])
    ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Welch Interval 3 Peak')

    ax = plt.subplot(246)
    plt.plot(times, df['vaccel_peak_int3'])
    ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Welch Interval 3 Peak')

    ax = plt.subplot(247)
    plt.plot(times, df['haccel_peak_int4'])
    ax.set_title('Horiz. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Welch Interval 4 Peak')

    ax = plt.subplot(248)
    plt.plot(times, df['vaccel_peak_int4'])
    ax.set_title('Vert. Accel.'), ax.set_xlabel('Time (s)'), ax.set_ylabel('Welch Interval 4 Peak')

    plt.tight_layout()
    plt.savefig(bearing + '_freq_domain_features.png')
    plot_num += 1

plt.show()
