from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import os
import joblib
import pandas as pd
from config import API_KEY, CITY

app = FastAPI(title="Weather Intelligence Platform 🚀")

templates = Jinja2Templates(directory="templates")

BASE_URL = "https://api.weatherapi.com/v1/current.json"


# -----------------------------
# Safe Model Loading
# -----------------------------
model = None
if os.path.exists("weather_model.pkl"):
    try:
        model = joblib.load("weather_model.pkl")
        print("✅ ML model loaded successfully.")
    except Exception as e:
        print("⚠ Error loading model:", e)


# -----------------------------
# Home Route
# -----------------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# -----------------------------
# Current Weather Endpoint
# -----------------------------
@app.get("/current-weather")
def current_weather(city: str = CITY):

    try:
        params = {
            "key": API_KEY,
            "q": city
        }

        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="City not found or API error")

        data = response.json()

        return {
            "city": data["location"]["name"],
            "region": data["location"]["region"],
            "country": data["location"]["country"],
            "temperature": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"],
            "condition": data["current"]["condition"]["text"],
            "wind_kph": data["current"]["wind_kph"]
        }

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Weather service unavailable")


# -----------------------------
# ML Prediction Endpoint
# -----------------------------
@app.get("/predict")
def predict_temperature(humidity: float, wind_kph: float):

    if model is None:
        raise HTTPException(status_code=400, detail="Model not trained yet")

    try:
        input_data = pd.DataFrame([[humidity, wind_kph]],
                                  columns=["humidity", "wind_kph"])

        prediction = model.predict(input_data)

        return {
            "predicted_temperature": round(float(prediction[0]), 2)
        }

    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed")


# -----------------------------
# Dashboard UI Route
# -----------------------------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})