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

# File path for saving data
file_path = 'C:\\Users\\biauser\\PycharmProjects\\PythonProject\\24_hour_forecast.csv'


# Function to fetch 24-hour hourly forecast
def fetch_hourly_forecast(lat, lon, api_key):
    url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()


# Save forecast data to CSV
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write headers
    writer.writerow([
        'city', 'country', 'date_time', 'temperature_celsius', 'feels_like_celsius',
        'temperature_min_celsius', 'temperature_max_celsius', 'weather',
        'pressure', 'humidity', 'wind_speed', 'wind_deg', 'lat', 'lon'
    ])

    for city, (lat, lon) in cities.items():
        data = fetch_hourly_forecast(lat, lon, API_KEY)

        if 'list' in data:
            for entry in data['list'][:24]:  # Limit to next 24 hours
                writer.writerow([
                    city,
                    "CA",
                    datetime.fromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S'),
                    round(entry['main']['temp'], 2),
                    round(entry['main']['feels_like'], 2),
                    round(entry['main'].get('temp_min', entry['main']['temp']), 2),
                    round(entry['main'].get('temp_max', entry['main']['temp']), 2),
                    entry['weather'][0]['description'],
                    entry['main']['pressure'],
                    entry['main']['humidity'],
                    entry['wind']['speed'],
                    entry['wind']['deg'],
                    lat,
                    lon
                ])

print("Saved 24-hour forecast data to 24_hour_forecast.csv")
