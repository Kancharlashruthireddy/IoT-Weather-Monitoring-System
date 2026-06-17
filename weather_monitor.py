from datetime import datetime

temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
air_quality = int(input("Enter Air Quality Index: "))

print("\nWeather Report")
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Air Quality:", air_quality)

print("Recorded At:", datetime.now())
