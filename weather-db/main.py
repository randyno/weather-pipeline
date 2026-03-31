import requests
from datetime import datetime, timedelta
import json

def get_weather():
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
    
    print(f"Fetching weather data from URL: {URL}")
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None
    
if __name__ == '__main__':
    json_data = get_weather()
    if json_data:
        with open(f'/app/data/raw/open-meteo-{datetime.now().strftime("%Y-%m-%d %H-%M")}.json', 'w') as f:
            json.dump(json_data, f, indent=2)