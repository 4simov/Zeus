
import datetime
import sys
import time
import requests
import json

baseUrl = "http://127.0.0.1:5000"
address = 0x76
add = 0x77
while True:
    try:

        # Extract temperature, pressure, and humidity
        temperature_celsius = 15
        pressure = 20
        humidity = 20
        date = str(datetime.datetime.now())

        r = requests.post(baseUrl + '/re', json={
  		"temperature": temperature_celsius,
  		"humidite": humidity,
        "sonde_id": str(add),
        "date": date
	})
        print(f"Status Code: {r.status_code}, Response: {r.json()}")
        # Wait for a few seconds before the next reading
        time.sleep(10)

    except KeyboardInterrupt:
        print('Program stopped')
        break
    except Exception as e:
        print('An unexpected error occurred:', str(e))
        break