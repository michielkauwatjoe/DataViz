#!/usr/bin/env python3

import knmi

# Pandas DataFrame.
df = knmi.get_day_data_dataframe(stations=[260])

print('Description')
print(df.describe())
print('Data Frame')
print(df)
