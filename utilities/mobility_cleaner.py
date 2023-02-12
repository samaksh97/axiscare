import pandas as pd
import numpy as np
import csv

df = pd.read_csv('mobility.csv')  
# df = df.reset_index() 
df = df.fillna(0)
unique_vals = df.location_key.unique()

us_vals = []
for uv in unique_vals:
    try:
        if 'US_' in uv:
            us_vals.append(uv)
    except:
        pass
usv = []
for x in us_vals:
    if x.count('_')== 1:
        usv.append(x)

print(len(usv))
df3 = df[df['location_key'].isin(usv)]
df3.to_csv('mobility_cummulative.csv') 

