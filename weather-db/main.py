import requests
from datetime import datetime, timedelta
from pandas import read_csv, to_datetime
import csv
import json


def get_weather_data():
    """Fetch weather data from the Open-Meteo API and return it as JSON.
    Returns:
        dict: A dictionary containing the weather data.
    """
    base_url = "https://api.open-meteo.com/v1/forecast?"
    start_date = datetime(2026, 3, 1).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    Latitude, Longitude = 49.683333, 1.400000  # Massy, France
    
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

def get_open_meteo_data_start_date(start_date_str:str):
    """Fetch weather data from the Open-Meteo API starting from a specific date until the current date.
    Args:
        start_date_str (str): The start date in the format 'YYYY-MM-DD'.
    Returns:
        dict: A dictionary containing the weather data.
    """
    base_url = "https://api.open-meteo.com/v1/forecast?"
    end_date = datetime.now().strftime('%Y-%m-%d')
    Latitude, Longitude = 49.683333, 1.400000  # Massy, France
    
    required_data = "hourly=temperature_2m,relative_humidity_2m,apparent_temperature,rain,cloud_cover,wind_speed_10m,precipitation"
    models = "models=meteofrance_seamless"

    URL = f"{base_url}"\
        + f"&start_date={str(start_date_str)}&end_date={str(end_date)}" \
        + f"&latitude={Latitude}&longitude={Longitude}" \
        + f"&{required_data}&{models}"
    
    response = requests.get(URL)
    if response.status_code == 200:
        print(f"Weather data successfully fetched from Open-Meteo API "\
              +f"starting from {start_date_str}.", flush=True)
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}", flush=True)
        return None

def json_to_csv(json_source:str, csv_destination:str, _create_destination=False):
    """
    Extracts only the useful weather data from the json_source file
     and saves it in the {csv_destination}.csv file in /data/dbt_raw/ for the dbt pipelines.
    
    Args:
        json_source (str): The name of the JSON file containing the weather data collected from Open-Meteo API.
        csv_destination (str): The name of the CSV file at the end of which data will be added.
        _create_destination(Bool): is True if the csv file does not exists yet and needs being created
    """
    rep, insertion_time = '/app/data/', f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    with open(f'{rep}/raw/{json_source}.json', 'r') as f:
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

            header = ['insertion_time', 'datetime_hour', 'temperature_2m', 'relative_humidity_2m', 
                      'apparent_temperature', 'rain', 'cloud_cover', 'wind_speed_10m', 'precipitation']
            rows = zip(_insertion_time, times, temperature_2m, relative_humidity_2m, 
                       apparent_temperature, rain, cloud_cover, wind_speed_10m, precipitation)

            with open(f'{rep}/dbt_raw/{csv_destination}.csv', mode = 'a' \
                , newline = '\n') as raw_csv_file: # Add data at the end of the csv file
                write = csv.writer(raw_csv_file)
                if _create_destination:
                    write.writerow(header)
                write.writerows(rows)
                print(f"Weather data successfully saved to {rep}/dbt_raw/{csv_destination}.csv")

def download_missing_data(data_rep:str,csv_file_name:str, date_column_name:str='datetime_hour') -> int:
    """
    Checks if the {csv_file_name}.csv file contains up-to-date weather data.
    If not (up to the current date), it fetches the missing data from the Open-Meteo API 
    and appends it to the existing CSV file.
    
    Args:
        data_rep: The directory where all data is stored.
        csv_file_name: The name of the CSV file to check and update (without the .csv extension).
        date_column_name: The name of the column in the CSV file that contains the 
                datetime information (default is 'datetime_hour') as a '%Y-%m-%dT%H:%M' string.

    Returns: 
        0: if the data is already up-to-date, 
        1: if new data was fetched and appended to the CSV file.
    """
    try:
        # Open the data file and check the most recent date in {date_column_name}
        weather_data = read_csv(f"{data_rep}/dbt_raw/{csv_file_name}.csv")
        weather_data[date_column_name] = to_datetime(weather_data[date_column_name], format='%Y-%m-%dT%H:%M')
        max_date = weather_data[date_column_name].max()
        # breakpoint()
        if max_date < datetime.now(): # The most recent date is before right now 
            print(f"Data in {data_rep}/dbt_raw/{csv_file_name}.csv is not up-to-date. ")
            print(f"Fetching missing weather data from the Open-Meteo API starting from " \
                 + f"{ (max_date + timedelta(days=-1)) }" )
            
            # -> Fetch more data. We move back to make sure there is no data gap.
            next_start_date = (max_date + timedelta(days=-1)).strftime('%Y-%m-%d')
            json_data = get_open_meteo_data_start_date(next_start_date)
            # breakpoint()
            if json_data:
                json_dest = csv_file_name + f'-{datetime.now().date()}'
                with open(f'{data_rep}/raw/{json_dest}.json', 'w') as f:
                    json.dump(json_data, f, indent=2) 
                print(f"Weather data successfully added to {data_rep}/raw/{json_dest}.json")

                # Save data as CSV file for dbt pipelines
                json_to_csv(json_source=json_dest, csv_destination=csv_file_name) 
                # breakpoint()
                return 1
        else:
            print(f"Data in {data_rep}/{csv_file_name}.csv is already up-to-date.")
            return 0
    except FileNotFoundError:
        print(f"File {data_rep}/dbt_raw/{csv_file_name}.csv does not exist yet.\nFetching all available data from the Open-Meteo API starting on March 1rst.")
        json_data = get_weather_data()
        # breakpoint()
        if json_data:
            with open(f'{data_rep}/raw/{csv_file_name}.json', 'w') as f:
                json.dump(json_data, f, indent=2) # Save data as Json file
            print(f"Weather data successfully saved to {data_rep}/raw/{csv_file_name}.json")
            json_to_csv(json_source=csv_file_name, 
                        csv_destination=csv_file_name,
                        _create_destination=True) # Save data as CSV file for dbt pipelines
            # breakpoint()
            return 1
    except Exception as e:
        print(f"An error occurred while checking or updating the weather data: {e}")
        print("error Message : "+ e.__str__())

    return 0
    
            
if __name__ == '__main__':
    rep = '/app/data'
    json_file_name = "open-meteo-weather-data"
    # json_data = get_weather_data()
    # if json_data:
    #     with open(f'{rep}/raw/{json_file_name}.json', 'w') as f:
    #         json.dump(json_data, f, indent=2) # Save data as Json file
    #     print(f"Weather data successfully saved to {rep}/raw/{json_file_name}.json")
    #     json_to_csv(json_file_name, json_file_name) # Save data as CSV file for dbt pipelines
    download_missing_data(data_rep=rep, csv_file_name=json_file_name)