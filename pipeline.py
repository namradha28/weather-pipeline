"""
pipeline.py

Main orchestrator for Weather Data Pipeline
Extract → Transform → Load (ETL)
"""

import logging
from datetime import datetime
from extract import extract_weather
from transform import transform_weather
from load import load_to_db


# -----------------------------
# Configure Logging
# -----------------------------
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline():
    """
    Runs the full ETL pipeline.
    """

    try:
        logging.info("🚀 Pipeline started")

        # -----------------------------
        # 1️⃣ Extract
        # -----------------------------
        logging.info("Extracting weather data...")
        raw_data = extract_weather()

        # -----------------------------
        # 2️⃣ Transform
        # -----------------------------
        logging.info("Transforming weather data...")
        df = transform_weather(raw_data)

        # Add timestamp column
        df["timestamp"] = datetime.now()

        # -----------------------------
        # 3️⃣ Load
        # -----------------------------
        logging.info("Loading data into database...")
        load_to_db(df)

        logging.info("✅ Pipeline completed successfully")
        print("Pipeline executed successfully!")

    except Exception as e:
        logging.error(f"❌ Pipeline failed: {str(e)}")
        print("Pipeline failed. Check pipeline.log for details.")


# -----------------------------
# Run as Script
# -----------------------------
if __name__ == "__main__":
    run_pipeline()