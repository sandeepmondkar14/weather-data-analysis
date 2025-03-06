import requests
import csv
from datetime import datetime

# Define the function to fetch weather data for a given city
def fetch_weather_data(city, country, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': f'{city},{country}',
        'appid': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Convert temperature from Kelvin to Celsius
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    # Process data
    processed_data = {
        'city': data['name'],
        'country': country,
        'temperature_celsius': round(kelvin_to_celsius(data['main']['temp']), 2),
        'feels_like_celsius': round(kelvin_to_celsius(data['main']['feels_like']), 2),
        'temperature_min_celsius': round(kelvin_to_celsius(data['main']['temp_min']), 2),
        'temperature_max_celsius': round(kelvin_to_celsius(data['main']['temp_max']), 2),
        'weather': data['weather'][0]['description'],
        'lat': data['coord']['lat'],
        'lon': data['coord']['lon'],
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'wind_speed': data['wind']['speed'],
        'wind_deg': data['wind']['deg'],
        'visibility': data.get('visibility', 0),  # Default to 0 if visibility is not provided
        'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),  # Convert Unix timestamp to datetime
        'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S'),  # Convert Unix timestamp to datetime
        'datetimestamp': datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S')  # Convert Unix timestamp to datetime
    }

    return processed_data

# Define cities to fetch weather data for
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

# Save processed data to a CSV file
file_path = 'C:\\Users\\biauser\\PycharmProjects\\PythonProject\\weather_data.csv'  # Update the path to your CSV file
with open(file_path, 'w', newline='') as file:  # 'w' mode to overwrite the file
    writer = csv.writer(file)
    # Write headers
    writer.writerow([
        'city', 'country', 'temperature_celsius', 'feels_like_celsius', 'temperature_min_celsius', 'temperature_max_celsius',
        'weather', 'lat', 'lon', 'pressure', 'humidity', 'wind_speed', 'wind_deg', 'visibility', 'sunrise', 'sunset', 'datetimestamp'
    ])

    for city in cities:
        data = fetch_weather_data(city, country, api_key)
        writer.writerow(data.values())

print("New CSV file created and data written to weather_data.csv")
