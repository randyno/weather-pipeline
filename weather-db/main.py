import requests
from datetime import datetime, timedelta
import csv
import json

def get_weather_data():
    """Fetch weather data from the Open-Meteo API and return it as JSON.
    Returns:
        dict: A dictionary containing the weather data.
    """
    base_url = "https://api.open-meteo.com/v1/forecast?"
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=1)
    Latitude, Longitude = 49.683333, 1.400000  # Massy, France
    # &latitude=52.52&longitude=13.41&
    required_data = "hourly=temperature_2m,relative_humidity_2m,apparent_temperature,rain,cloud_cover,wind_speed_10m,precipitation"
    models = "models=meteofrance_seamless"

    URL = f"{base_url}" \
        + f"&start_date={str(start_date)}&end_date={str(end_date)}" \
        + f"&latitude={Latitude}&longitude={Longitude}" \
        + f"&{required_data}&{models}"
    
    print(f"Fetching weather data from URL: {URL}", flush=True)
    response = requests.get(URL)
    if response.status_code == 200:
        print("Weather data successfully fetched from Open-Meteo API.", flush=True)
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}", flush=True)
        return None

def json_to_csv(json_file_name):
    """Extracts only the useful weather data from the JSON dictionnary
     and saves it as a .csv file in /data/dbt_raw/ for the dbt pipelines.
    Args:
        json_data (dict): The JSON data containing the weather information collected from Open-Meteo API.
    """
    rep, insertion_time = '/app/data/', f"{datetime.now().strftime('%Y-%m-%d %H-%M')}"
    with open(f'{rep}/raw/{json_file_name}.json', 'r') as f:
        json_data = json.load(f)
    
    if json_data is not None:
        hourly_weather_data = json_data.get("hourly")
        if hourly_weather_data:
            _insertion_time = [insertion_time] * len(hourly_weather_data['time'])
            times = hourly_weather_data['time']
            temperature_2m = hourly_weather_data['temperature_2m']
            relative_humidity_2m = hourly_weather_data['relative_humidity_2m']
            apparent_temperature = hourly_weather_data['apparent_temperature']
            rain = hourly_weather_data['rain']
            cloud_cover = hourly_weather_data['cloud_cover']
            wind_speed_10m = hourly_weather_data['wind_speed_10m']
            precipitation = hourly_weather_data['precipitation']
            header = ['insertion_time', 'datetime_hour', 'temperature_2m', 'relative_humidity_2m', 'apparent_temperature', 'rain', 'cloud_cover', 'wind_speed_10m', 'precipitation']

            rows = zip(_insertion_time, times, temperature_2m, relative_humidity_2m, apparent_temperature, rain, cloud_cover, wind_speed_10m, precipitation)
            with open(f'{rep}/dbt_raw/{json_file_name}.csv', mode = 'w' \
                , newline = '') as raw_csv_file:
                write = csv.writer(raw_csv_file)
                write.writerow(header)
                write.writerows(rows)
                print(f"Weather data successfully saved to {rep}/dbt_raw/{json_file_name}.csv")

            
if __name__ == '__main__':
    json_data = get_weather_data()
    rep = '/app/data/'
    json_file_name = f"open-meteo-{datetime.now().strftime('%Y-%m-%d %H-%M')}"
    if json_data:
        print("Weather data successfully fetched from Open-Meteo API.")
        with open(f'{rep}/raw/{json_file_name}.json', 'w') as f:
            json.dump(json_data, f, indent=2) # Save data as Json file
        print(f"Weather data successfully saved to {rep}/raw/{json_file_name}.json")
        json_to_csv(json_file_name) # Save data as CSV file for dbt pipelines