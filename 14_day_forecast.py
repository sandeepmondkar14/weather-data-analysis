import requests
import csv
from datetime import datetime

# Updated city coordinates
cities = {
    'Vancouver': (49.2497, -123.1193),
    'Victoria': (48.4329, -123.3693),
    'Calgary': (51.0501, -114.0853),
    'Edmonton': (53.5501, -113.4687),
    'Regina': (50.4501, -104.6178),
    'Saskatoon': (52.1168, -106.6345),
    'Winnipeg': (49.8844, -97.1470),
    'Toronto': (43.7001, -79.4163),
    'Ottawa': (45.4112, -75.6981),
    'Montreal': (45.5088, -73.5878),
    'Québec': (46.8123, -71.2145),
    'Fredericton': (45.9454, -66.6656),
    'Saint John': (45.2727, -66.0677),
    'Halifax': (44.6453, -63.5724),
    'Dartmouth': (44.6713, -63.5772),
    'Charlottetown': (46.2352, -63.1267),
    "St. John's": (47.5649, -52.7093)
}

# OpenWeatherMap API key (Replace with your actual API key)
API_KEY = "2036eaffa8902c0cc986a19c9984398a"

# Number of days (max 16 for this API)
DAYS = 14

# File path for saving data
file_path = 'C:\\Users\\biauser\\PycharmProjects\\PythonProject\\14_day_forecast.csv'


# Function to fetch 14-day daily forecast
def fetch_daily_forecast(lat, lon, api_key, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={days}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()


# Save forecast data to CSV
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write headers
    writer.writerow([
        'city', 'country', 'date', 'temperature_celsius', 'feels_like_celsius',
        'temperature_min_celsius', 'temperature_max_celsius', 'weather',
        'pressure', 'humidity', 'wind_speed', 'wind_deg', 'lat', 'lon'
    ])

    for city, (lat, lon) in cities.items():
        data = fetch_daily_forecast(lat, lon, API_KEY, DAYS)

        if 'list' in data:
            for day in data['list']:
                writer.writerow([
                    city,
                    "CA",
                    datetime.fromtimestamp(day['dt']).strftime('%Y-%m-%d'),
                    round(day['temp']['day'], 2),
                    round(day['feels_like']['day'], 2),
                    round(day['temp'].get('min', day['temp']['day']), 2),
                    round(day['temp'].get('max', day['temp']['day']), 2),
                    day['weather'][0]['description'],
                    day['pressure'],
                    day['humidity'],
                    day['speed'],  # Wind speed
                    day['deg'],  # Wind direction
                    lat,
                    lon
                ])

print("Saved 14-day forecast data to 14_day_forecast.csv")
