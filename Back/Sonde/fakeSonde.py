
import datetime
import sys
import threading
import time
import requests
import json

class SondeThread( threading.Thread) :
    baseUrl = "http://127.0.0.1:5000"
    address1 = 0x76
    address2 = 0x77
    idSonde= ""
    isActivate = False
    def __init__(self, sonde) :
        super(SondeThread, self).__init__()
        self.idSonde = sonde

    def close(self) :
        self.activate = False

    def run(self) :
        
        while self.isActivate:
            try:
                if self.isActivate == False :
                    return "Désactivation de la sonde " + self.idSonde
                # Extract temperature, pressure, and humidity
                temperature_celsius = 15
                pressure = 20
                humidity = 20
                date = str(datetime.datetime.now())

                r = requests.post(self.baseUrl + '/re', json={
                    "temperature": temperature_celsius,
                    "humidite": humidity,
                    "sonde_id": str(self.idSonde),
                    "date": date
                })
                r2 = requests.put(self.baseUrl +'/sonde/' + self.idSonde, json = {
                    "activation" : False 
                })
                print(f"Status Code: {r.status_code}, Response: {r.json()}")
                print(f"Status Code: {r2.status_code}, Response: {r2.json()}")
                # Wait for a few seconds before the next reading
                time.sleep(10)

            except KeyboardInterrupt:
                print('Program stopped')
                break
            except Exception as e:
                print('An unexpected error occurred:', str(e))
                break
        
        return "Désactivation de la sonde " + self.idSonde
    