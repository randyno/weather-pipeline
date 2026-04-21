import os
import pandas as pd

class TestWeather_db:
    data_relative_path = "../data/dbt_raw/"
    raw_data_file_name = "open-meteo-weather-data.csv"
            
    def test_raw_data_exists(self):
        file_path =  self.data_relative_path + self.raw_data_file_name
        raw_data_exists = os.path.exists(file_path)
        assert raw_data_exists
