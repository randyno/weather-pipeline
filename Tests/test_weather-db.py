from pandas import read_csv, to_datetime
from datetime import datetime, timezone
import os
import pytest

class TestWeather_db:
    
    @pytest.mark.dependency(name="data_exists")
    def test_raw_data_exists(self, data_config):
        file_path =  data_config['data_relative_path'] + data_config['raw_data_file_name']
        raw_data_exists = os.path.exists(file_path)

        assert raw_data_exists, f"Le fichier open-meteo-weather-data.csv n'existe pas."
    
    @pytest.mark.dependency(depends = ["data_exists"], name="correct_structure")
    def test_data_structure(self, data_config):
        file_path =  data_config['data_relative_path'] + data_config['raw_data_file_name']
        weather_data = read_csv(file_path)
        actual_columns= set(weather_data.columns)
        expected_columns = set(data_config['weather_data_columns'])
        assert expected_columns.issubset(actual_columns), f"Colonnes manquantes : {(expected_columns - actual_columns)}"
    
    # TODO
    # Add a test on API responses



    # @pytest.mark.dependency(depends = ["data_exists","correct_structure"])
    # def test_data_is_continuous(self, data_config):
    #     # Recuperer toutes les dates et heures dans les donnees telechargees
    #     file_path =  data_config['data_relative_path'] + data_config['raw_data_file_name']
    #     weather_data = read_csv(file_path)
    #     days = to_datetime(weather_data["datetime_hour"]).dt.date
        
    #     actual_dates = set(days)
    #     expected_dates = set(data_config['expected_dates'])

    #     missing_dates = []
    #     for _day in expected_dates:
    #         if _day not in actual_dates:
    #             missing_dates.append(str(_day))

    #     assert len(missing_dates) == 0, f"Dates manquantes : {missing_dates}"
            
    
    

        

