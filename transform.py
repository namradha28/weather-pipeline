import pandas as pd

def transform_weather(data):
    weather_data = {
        "city": data["location"]["name"],
        "region": data["location"]["region"],
        "country": data["location"]["country"],
        "temperature_c": data["current"]["temp_c"],
        "humidity": data["current"]["humidity"],
        "condition": data["current"]["condition"]["text"],
        "wind_kph": data["current"]["wind_kph"]
    }

    df = pd.DataFrame([weather_data])
    return df