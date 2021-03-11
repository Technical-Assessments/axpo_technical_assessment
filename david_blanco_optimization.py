import pandas as pd
import numpy as np
import time

speed_df = pd.read_csv("DataOps_test/dataset_speed_optimization.csv")


########################################################################################

def function_to_apply(lat, lon):
    a = np.sin(lat / 2) ** 2 + np.cos(lon) * np.sin(lon / 2) ** 2

    return a


df = speed_df.copy()

start = time.time()

list_results = []
for i in range(0, len(df)):
    r = function_to_apply(df.iloc[i]['latitude'], df.iloc[i]['longitude'])
    list_results.append(r)

df['distance'] = list_results

elapsed_time_fl = (time.time() - start)
print(f"Time taken using iloc: {elapsed_time_fl}")

########################################################################################

df = speed_df.copy()

start = time.time()

df['distance'] = np.sin(df['latitude']/2)**2 + np.cos(df['longitude']) * np.sin(df['longitude']/2)**2
elapsed_time_fl = (time.time() - start)

print(f"Time taken when creating a new column with NumPy: {elapsed_time_fl}")