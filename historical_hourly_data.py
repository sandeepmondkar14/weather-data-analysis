import requests
import csv
from datetime import datetime, timedelta
import time

# List of cities
cities = [
    'Vancouver', 'Victoria',  # British Columbia
    'Calgary', 'Edmonton',  # Alberta
    'Regina', 'Saskatoon',  # Saskatchewan
    'Winnipeg',  # Manitoba
    'Toronto', 'Ottawa',  # Ontario
    'Montreal', 'Quebec City',  # Quebec
    'Fredericton', 'Saint John',  # New Brunswick
    'Halifax', 'Dartmouth',  # Nova Scotia
    'Charlottetown',  # Prince Edward Island
    "St. John's"  # Newfoundland and Labrador
]
country = 'CA'
api_key = '2036eaffa8902c0cc986a19c9984398a'  # Replace with your actual API key

# Function to fetch historical hourly weather data for the past 24 hours
def fetch_historical_hourly_data(city, country, api_key):
    url = f"https://history.openweathermap.org/data/2.5/history/city?q={city},{country}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

# Save historical hourly data to CSV
file_path = 'C:\\Users\\biauser\\PycharmProjects\\PythonProject\\historical_hourly_data.csv'  # Update the path to your CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write headers
    writer.writerow([
        'city', 'country', 'temperature_celsius', 'feels_like_celsius', 'temperature_min_celsius', 'temperature_max_celsius',
        'weather', 'pressure', 'humidity', 'wind_speed', 'wind_deg', 'datetimestamp'
    ])

    for city in cities:
        data = fetch_historical_hourly_data(city, country, api_key)
        if 'list' in data:
            for entry in data['list']:
                writer.writerow([
                    city,
                    country,
                    round(entry['main']['temp'] - 273.15, 2),
                    round(entry['main']['feels_like'] - 273.15, 2),
                    round(entry['main'].get('temp_min', entry['main']['temp']) - 273.15, 2),
                    round(entry['main'].get('temp_max', entry['main']['temp']) - 273.15, 2),
                    entry['weather'][0]['description'],
                    entry['main']['pressure'],
                    entry['main']['humidity'],
                    entry['wind']['speed'],
                    entry['wind']['deg'],
                    datetime.fromtimestamp(entry['dt']).strftime('%Y-%m-%d %H:%M:%S')
                ])
        time.sleep(1)  # To avoid hitting API rate limits
print("Saved historical hourly data to historical_hourly_data.csv")
