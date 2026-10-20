import requests

LAT, LON = 39.4143, -77.4105  # Frederick, MD

resp = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": LAT,
        "longitude": LON,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "temperature_unit": "fahrenheit",
        "wind_speed_unit": "mph",
        "timezone": "auto",
        "forecast_days": 1,
    },
    timeout=10,
)
resp.raise_for_status()
data = resp.json()

now, today = data["current"], data["daily"]
print("Today's weather in Frederick, MD")
print(f"  Now      : {now['temperature_2m']}°F")
print(f"  High/Low : {today['temperature_2m_max'][0]}°F / {today['temperature_2m_min'][0]}°F")
print(f"  Rain     : {today['precipitation_probability_max'][0]}% chance")
print(f"  Humidity : {now['relative_humidity_2m']}%")
print(f"  Wind     : {now['wind_speed_10m']} mph")