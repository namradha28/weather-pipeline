import pandas as pd
import sqlite3
from config import DB_NAME

def get_training_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT * FROM weather_data", conn)
    conn.close()

    return df