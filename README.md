# 🌦️ Weather Data Pipeline 🚀

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![API](https://img.shields.io/badge/API-Weather-green)
![ETL](https://img.shields.io/badge/Type-ETL_Pipeline-orange)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)
![Logging](https://img.shields.io/badge/Logging-Enabled-yellow)
![Architecture](https://img.shields.io/badge/Architecture-Modular-blueviolet)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> 🔥 A production-style Weather ETL pipeline built using Python that fetches real-time weather data from an API, processes it, logs execution stages, and stores structured output with proper failure handling.

---

# 🎯 Project Overview

This project simulates a real-world **Data Engineering workflow**.

It performs:

- 🌤 Real-time API data ingestion  
- 🧹 JSON validation & transformation  
- 📝 Execution logging  
- ❌ Failure-safe handling  
- 💾 Structured data storage  

Designed to reflect production-ready backend practices.

---

# 🏗️ Architecture

```
            ┌────────────────┐
            │   Weather API  │
            └───────┬────────┘
                    │
            ┌───────▼────────┐
            │  Data Fetching │
            └───────┬────────┘
                    │
            ┌───────▼────────┐
            │  Validation    │
            └───────┬────────┘
                    │
            ┌───────▼────────┐
            │ Transformation │
            └───────┬────────┘
                    │
            ┌───────▼────────┐
            │   JSON Output  │
            └────────────────┘
```

---

# ⚡ Features

✔ Real-time weather API integration  
✔ Configurable city parameter  
✔ Structured JSON transformation  
✔ Centralized logging system  
✔ Graceful API failure handling  
✔ Modular architecture  
✔ Easily extendable to AWS / Airflow  

---

# 📂 Project Structure

<details>
<summary>📁 Click to Expand</summary>

```
weather-pipeline/
│
├── pipeline.py        # Main pipeline execution
├── config.py          # API configuration
├── logger.py          # Logging setup
├── utils.py           # Helper functions
├── output/
│   └── weather.json
└── README.md
```

</details>

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/weather-pipeline.git
cd weather-pipeline
```

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 3️⃣ Add API Key

Inside `config.py`:

```python
API_KEY = "your_api_key_here"
CITY = "Delhi"
```

---

# ▶️ Running the Pipeline

```bash
python pipeline.py
```

---

## ✅ Successful Execution

```
🚀 Pipeline started
🌤 Fetching weather data...
✅ Data fetched successfully
💾 Data stored successfully
🎉 Pipeline completed
```

---

## ❌ Failure Handling Example

```
🚀 Pipeline started
🌤 Fetching weather data...
❌ Pipeline failed: API Request Failed
```

✔ Logs error  
✔ Stops safely  
✔ Prevents corrupted output  

---

# 📊 Sample Output

```json
{
  "city": "Delhi",
  "temperature": 29,
  "humidity": 62,
  "condition": "Cloudy",
  "timestamp": "2026-02-26T10:48:13"
}
```

---

# 🚀 Future Enhancements

- ☁ Deploy to AWS Lambda  
- 🔁 Schedule using Apache Airflow  
- 🗄 Store data in MongoDB / PostgreSQL  
- 📊 Connect to Power BI dashboard  
- 📈 Add anomaly detection  
- 🐳 Dockerize the pipeline  
- 🧪 Add unit testing & CI/CD  

---

# 📈 Skills Demonstrated

- API Integration  
- ETL Pipeline Design  
- Logging & Monitoring  
- Exception Handling  
- Modular Backend Architecture  
- Debugging Production Errors  

---

# 🏆 Why This Project Matters

This project demonstrates:

✔ Backend engineering fundamentals  
✔ Real-world data ingestion  
✔ Failure-safe execution  
✔ Scalable design thinking  
✔ Clean project organization  

Ideal for:
- Data Engineer roles  
- Backend Developer roles  
- Cloud Engineer roles  

---

# ⭐ Support

If you found this project helpful:

- ⭐ Star the repository  
- 🍴 Fork it  
- 💬 Share feedback  
