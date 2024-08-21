CREATE DATABASE weather_db;

\c weather_db

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city_name TEXT NOT NULL,
    city_id INTEGER NOT NULL,
    country_code CHAR(2),
    latitude NUMERIC(8, 5),
    longitude NUMERIC(8, 5),
    timestamp TIMESTAMP NOT NULL,
    weather_main TEXT,
    weather_description TEXT,
    temperature NUMERIC(5, 2),
    feels_like NUMERIC(5, 2),
    pressure INTEGER,
    humidity INTEGER,
    visibility INTEGER,
    wind_speed NUMERIC(5, 2),
    wind_deg INTEGER,
    clouds INTEGER,
    sunrise TIMESTAMP,
    sunset TIMESTAMP
);

-- Grant user privileges, replace `your_user_name`
-- Uncomment and modify the following lines as needed
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO your_user_name;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO your_user_name;

-- Insert initial data (optional)
-- Example initial data insertion
-- INSERT INTO weather_data (city_name, city_id, country_code, latitude, longitude, timestamp, weather_main, weather_description, temperature, feels_like, pressure, humidity, visibility, wind_speed, wind_deg, clouds, sunrise, sunset)
-- VALUES ('Sample City', 12345, 'SC', 12.34567, 76.54321, '2024-08-21 12:00:00', 'Clear', 'Clear sky', 25.00, 24.00, 1013, 60, 10000, 5.00, 180, 10, '2024-08-21 06:00:00', '2024-08-21 18:00:00');