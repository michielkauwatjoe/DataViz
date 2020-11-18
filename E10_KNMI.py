#!/usr/bin/env python3

# https://knmi.nl/kennis-en-datacentrum/achtergrond/data-ophalen-vanuit-een-script
# https://github.com/EnergieID/KNMI-py
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

import knmi
from latlon import Latitude, Longitude

# Pandas DataFrame.
df = knmi.get_day_data_dataframe(stations=[260])


stations = knmi.stations.values()
sortedStations = sorted(stations, key=lambda s: s.name, reverse=False)

for station in sortedStations:
    lat = Latitude(station.latitude).to_string('d% %m% %S% %H')
    lon = Longitude(station.longitude).to_string('d% %m% %S% %H')

    # station.altitude
    print(' * %s, #%d, ll: (%s, %s)' % (station.name, station.number, lat, lon))

for key,value in knmi.variables.items():
    print(' * %s: %s' % (key,value))

print('Description')
print(df.describe())
print('Data Frame')
print(df)
