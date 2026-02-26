import requests
from config import API_KEY, CITY

BASE_URL = "https://api.weatherapi.com/v1/current.json"

def extract_weather():
    """
    Extract weather data from WeatherAPI
    """

    try:
        print("Calling WeatherAPI...")

        params = {
            "key": API_KEY,
            "q": CITY
        }

        response = requests.get(BASE_URL, params=params, timeout=10)

        print("Status Code:", response.status_code)
        print("Response:", response.text)

        # Raise error if request failed
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        raise Exception(f"WeatherAPI request failed: {e}")