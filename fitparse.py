import csv
import matplotlib.pyplot as plt
import os
from datetime import datetime
from collections import OrderedDict
import pandas as pd
import numpy as np

FIT_DIRECTORY = "ENTER FIT DATA DIRECTORY HERE"
data_keys = 'Distance (m),Calories (kcal),Average speed (m/s),Max speed (m/s),Min speed (m/s),Step count,Average weight (kg),Max weight (kg),Min weight (kg),Inactive duration (ms),Walking duration (ms),Running duration (ms),Biking duration (ms)'.split(',')

fit_data = []
for file in os.listdir(FIT_DIRECTORY)[:-2]:

    date = datetime.strptime(file, '%Y-%m-%d.csv')
    with open(os.path.join(FIT_DIRECTORY, file)) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            time = datetime.strptime(row['Start time'][:5], '%H:%M').time()
            row_datetime = datetime.combine(date, time)
            row_data = {'datetime': row_datetime}

            for key in data_keys:
                if key in row:
                    try:
                        row_data[key] = float(row[key])
                    except ValueError:
                        row_data[key] = None
                else:
                    row_data[key] = None
            fit_data.append(row_data)

df = pd.DataFrame(fit_data)
df.index = df['datetime']
df['time'] = pd.to_datetime(df['datetime'], format='%H:%M').dt.time

plt.figure()
day_list = [ group[1] for group in df.groupby([df.index.year, df.index.month, df.index.day]) ]

for day in day_list:
    # Replace all NaN references with 0's
    day.fillna(value={'Distance (m)': 0, 'Step count': 0}, inplace=True)

    # Plot of every day cumulative step count on one chart
    # plt.plot(day['time'].astype('O'), day['Step count'].cumsum())

    # Plot of every day cumulative distance on one chart
    # plt.plot(day['time'].astype('O'), day['Distance (m)'].cumsum())

# Plot of total step count cumulative some
# plt.ylim(bottom=0)
# plt.title('Cumulative Steps')
# plt.plot(df['datetime'].astype('O'), df['Step count'].cumsum())

# Count of total distance in km
# plt.title('Distance traveled (km)')
# plt.plot(df['datetime'].astype('O'), (df['Distance (m)'].cumsum() / 1000))

# Plot of an average of each day's step count
df.fillna(value={'Step count': 0}, inplace=True)

avg_df = df.groupby('time').agg([np.average])['Step count']
plt.plot(avg_df['time'], avg_df['average'])

# print value of highest step day
print(df.groupby([df.index.year, df.index.month, df.index.day])['Step count'].sum().idxmax())
plt.show()
