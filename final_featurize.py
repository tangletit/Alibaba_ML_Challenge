import pandas as pd

bearings = ['Bearing1_1', 'Bearing1_2', 'Bearing1_6', 'Bearing1_7']
for bearing in bearings:
    df_td = pd.read_csv(bearing + '_time_domain_features.csv')
    df_fd = pd.read_csv(bearing + '_freq_domain_features.csv')
    df = pd.DataFrame({'time': df_td['time'],
                       'haccel_var': df_td['haccel_var'],
                       'vaccel_var': df_td['vaccel_var'],
                       'haccel_trapz_int1': df_fd['haccel_trapz_int1'],
                       'RUL': 10*(len(df_td)-1) - df_td['time']})
    df.to_csv(bearing + '_final_features.csv', index=False)
