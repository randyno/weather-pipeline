from pathlib import Path
from pandas import to_datetime, date_range
from datetime import datetime
import os
import pytest

@pytest.fixture(autouse=True)
def setup_relative_path():
    # On sauvegarde le repertoire initial pour y revenir apres le test
    old_cwd = os.getcwd()

    # Changer le repertoire courant
    test_dir = Path(__file__).parent.resolve()
    os.chdir(test_dir)

    yield

    # Teardown : on retablit le repertoire initial
    os.chdir(old_cwd)

@pytest.fixture(autouse=True)
def data_config():
    start_date = to_datetime("2026-03-01").date()
    end_date = datetime.today().date()
    expected_dates = date_range(start=start_date, end=end_date).date

    return {
        "data_relative_path" : "../data/dbt_raw/",
        "raw_data_file_name" :"open-meteo-weather-data.csv",
        "weather_data_columns" : ["insertion_time","datetime_hour","temperature_2m",
                                "relative_humidity_2m", "apparent_temperature","rain",
                                "cloud_cover","wind_speed_10m","precipitation"],
        "expected_dates" : expected_dates
    }
