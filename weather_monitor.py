from datetime import datetime
import csv

temperature = float(input("Enter Temperature (°C): "))
humidity = float(input("Enter Humidity (%): "))
air_quality = int(input("Enter Air Quality Index: "))

timestamp = datetime.now()

with open("weather_data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        timestamp,
        temperature,
        humidity,
        air_quality
    ])

print("\nWeather Data Recorded Successfully")

if temperature > 35:
    print("High Temperature Alert!")

if humidity > 80:
    print("High Humidity Alert!")

if air_quality > 100:
    print("Poor Air Quality Alert!")
