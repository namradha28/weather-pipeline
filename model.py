from sklearn.linear_model import LinearRegression
from features import get_training_data
import joblib

def train_model():
    df = get_training_data()

    if len(df) < 5:
        print("Not enough data to train model.")
        return

    X = df[["humidity", "wind_kph"]]
    y = df["temperature_c"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "weather_model.pkl")
    print("Model trained and saved.")