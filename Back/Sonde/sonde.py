import sys
import time
import smbus2
import bme280
import requests
import prelevement
import statistics

baseUrl = "http://127.0.0.1:5000"
# BME280 sensor address (default address)
address = 0x76

# Initialize I2C bus
bus = smbus2.SMBus(1)

# Load calibration parameters
calibration_params = bme280.load_calibration_params(bus, address)
def celsius(far):
        return ((far-32)*5)/9

def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

def prelevement() :
    data = bme280.sample(bus, address, calibration_params)
    # Extract temperature, pressure, and humidity
    temperature_celsius = data.temperature
    pressure = data.pressure
    humidity = data.humidity

    # Convert temperature to Fahrenheit
    temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
    print(sys.argv[1])
        # Print the readings
    print("Temperature: {:.2f} °C, {:.2f} °F".format(temperature_celsius, temperature_fahrenheit))
    print("Pressure: {:.2f} hPa".format(pressure))
    print("Humidity: {:.2f} %".format(humidity))
    
    json={
        "temperature": temperature_celsius,
        "humidite": humidity
    }

    return json

    """r = requests.post(baseUrl + '/re', json={
  		"temperature": temperature_celsius,
  		"humidite": humidity
	})
    print(f"Status Code: {r.status_code}, Response: {r.json()}")
    # Wait for a few seconds before the next reading
    time.sleep(int(sys.argv[1]))"""

"""while True:
    try:
        # Read sensor data
        data = bme280.sample(bus, address, calibration_params)

        # Extract temperature, pressure, and humidity
        temperature_celsius = data.temperature
        pressure = data.pressure
        humidity = data.humidity

        # Convert temperature to Fahrenheit
        temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
        print(sys.argv[1])
        # Print the readings
        print("Temperature: {:.2f} °C, {:.2f} °F".format(temperature_celsius, temperature_fahrenheit))
        print("Pressure: {:.2f} hPa".format(pressure))
        print("Humidity: {:.2f} %".format(humidity))
        
        r = requests.post(baseUrl + '/re', json={
  		"temperature": temperature_celsius,
  		"humidite": humidity
	})
        print(f"Status Code: {r.status_code}, Response: {r.json()}")
        # Wait for a few seconds before the next reading
        time.sleep(int(sys.argv[1]))

    except KeyboardInterrupt:
        print('Program stopped')
        break
    except Exception as e:
        print('An unexpected error occurred:', str(e))
        break
"""
def realPrelevement() :
        listT = []
        listH = []
        n = 5
        i = 0
        rateLissage = 0.5

        while i < n:
            data = bme280.sample(bus, address, calibration_params)
            # Extract temperature, pressure, and humidity
            listT = data.temperature
            listH = data.humidity
            i += 1
            print(i)
            time.sleep(rateLissage)
        
        return prelevement.Prelevement(statistics.mean(listT), statistics.mean(listH))

