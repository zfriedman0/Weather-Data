import requests
import os
import psycopg2

from dotenv import load_dotenv
from datetime import datetime
from geopy.geocoders import Nominatim

load_dotenv()

key = os.getenv("API_KEY")
geolocator = Nominatim(user_agent="weather-data")

user_input = input("Enter a location: ")
location = geolocator.geocode(user_input)
print(f"Found {location.address}\nUsing {location.latitude}, {location.longitude}...")

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={location.latitude}&lon={location.longitude}&appid={key}&units=imperial")
weather_data = response.json()

conn = psycopg2.connect(f"dbname={os.getenv('DB_NAME')} user={os.getenv('DB_USER')} password={os.getenv('DB_PASS')}")
cur = conn.cursor()

sunrise = datetime.fromtimestamp(weather_data['city']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
sunset = datetime.fromtimestamp(weather_data['city']['sunset']).strftime('%Y-%m-%d %H:%M:%S')

for item in weather_data['list']:
    cur.execute("INSERT INTO weather_data (city_name, city_id, country_code, latitude, longitude, timestamp, weather_main, weather_description, temperature, feels_like, pressure, humidity, visibility, wind_speed, wind_deg, clouds, sunrise, sunset) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id;", 
                (weather_data['city']['name'], weather_data['city']['id'], weather_data['city']['country'],
                 weather_data['city']['coord']['lat'], weather_data['city']['coord']['lon'], item['dt_txt'],
                 item['weather'][0]['main'], item['weather'][0]['description'], item['main']['temp'], item['main']['feels_like'],
                 item['main']['pressure'], item['main']['humidity'], item['visibility'], item['wind']['speed'],
                 item['wind']['deg'], item['clouds']['all'], sunrise, sunset)
                )
    
weather_data_id = cur.fetchone()[0]

conn.commit()
cur.close()
conn.close()

#print(weather_data["list"][0]["main"]["temp"])