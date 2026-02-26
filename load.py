import sqlite3
from config import DB_NAME

def load_to_db(df):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            city TEXT,
            region TEXT,
            country TEXT,
            temperature_c REAL,
            humidity REAL,
            condition TEXT,
            wind_kph REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    df.to_sql("weather_data", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()