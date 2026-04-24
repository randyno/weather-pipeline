import os
from pathlib import Path
from pandas import read_csv, to_datetime
from datetime import datetime 

os.chdir(
    Path(__file__).parent.resolve()
)

weather_data = read_csv('data/dbt_raw/open-meteo-weather-data.csv', sep =',')
weather_data['datetime'] = to_datetime(weather_data['datetime_hour'])
print(weather_data['datetime'][:5])