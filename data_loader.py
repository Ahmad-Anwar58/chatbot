import pandas as pd

def load_sensor_data(filepath):
    try:
        df = pd.read_excel(filepath)
        df.fillna(method='ffill', inplace=True)
        return df
    except Exception as e:
        print(f"Error loading sensor data: {e}")
        return pd.DataFrame()

def get_latest_values(df):
    if df.empty:
        return {}
    latest = df.iloc[-1]
    return {
        "Soil Moisture": latest['Soil Moisture (%)'],
        "Soil Temperature": latest['Soil Temperature (°C)'],
        "Wind Speed": latest['Wind Speed (km/h)'],
        "Rainfall": latest['Rainfall (mm)'],
        "Pest Risk": latest['Pest Infestation Risk (%)'],
        "Yield Prediction": latest['Crop Yield Prediction (kg)'],
        "Irrigation Efficiency": latest['Irrigation Efficiency (%)'],
        "Fertilizer Usage": latest['Fertilizer Usage (kg)'],
        "Pesticide Usage": latest['Pesticide Usage (kg)'],
        "Soil Health": latest['Soil Health Index (0-100)']
    }
