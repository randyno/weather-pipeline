import pytest
from pathlib import Path


class TestWeather_dbt:

    @pytest.mark.dependency(name="exists")
    def test_database_exists(self, data_config):
        database_file = data_config['data_relative_path'] + "weather_" + data_config['target'] + ".duckdb"
        
        # Make sure the database file exists and is not empty
        assert Path(database_file).exists(), f"Le fichier base de donnee {database_file} n'existe pas."

    @pytest.mark.dependency(depends = ['exists'])
    def test_database_error(self, data_config):
        database_file = data_config['data_relative_path'] + "weather_" + data_config['target'] + ".duckdb"
        database_error_file = database_file + ".wal" 
        # This .duckdb.wal file stays if an error occurs when writing in the database file.

        assert Path(database_file).stat().st_size > 0, \
            f"Le fichier base de donnee est vide. Il n'y a pas de donnees"
        assert not Path(database_error_file).exists(), \
            f"Une erreur s'est produite lors de la derniere transaction. Les donnees sont corrompues."