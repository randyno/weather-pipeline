import streamlit as st
import duckdb
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="☁️",
    layout="wide"
)
st.title("WEATHER DASHBOARD ☁️")


# Connect to DuckDB
TARGET = 'dev'
@st.cache_resource # Cache the connection to avoid reconnecting on every interaction
def get_db_connection():
    database_path = f'/app/data/weather_{TARGET}.duckdb'
    conn = duckdb.connect(database=database_path,
                           read_only=True)
    return conn

if __name__ == "__main__":    
    # Load data from Database
    try:
        conn = get_db_connection()
        daily = pd.read_sql(f"SELECT * FROM weather_{TARGET}.daily_aggregates", conn)
        hourly = pd.read_sql(f"SELECT * FROM weather_{TARGET}.hourly_aggregates", conn)

        st.subheader("Daily Aggregates")
        st.write("The hottest day was on " \
                + str(daily[  daily['max_temperature_2m'] == daily['max_temperature_2m'].max()  ]['day'])\
                + " with a temperature of " + str(daily['max_temperature_2m'].max()) + "°C")
        
        st.subheader("Temperature Trends over the days")
        st.line_chart(daily.set_index('day')[['avg_temperature_2m', 'max_temperature_2m', 'min_temperature_2m']])
        st.subheader("Hourly Aggregates")
        st.write("The hottest hour was on " \
                + hourly[  hourly['max_temperature_2m'] == hourly['max_temperature_2m'].max()  ]['hours']\
                + " with a temperature of " + hourly['max_temperature_2m'].max().astype(str) + "°C")
    
        st.subheader("Temperature Trends within the day")
        st.line_chart(hourly.set_index('hours')[['avg_temperature_2m', 'max_temperature_2m', 'min_temperature_2m']])

    except Exception as e:
            st.error(f"Error connecting to the database: {e}") 
                    