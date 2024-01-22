import sys
import time
import smbus2
import bme280
import requests
import threading
import time
import json
import prelevement
import random
import statistics
import datetime

baseUrl = "http://10.121.128.165:5000/"

def celsius(far):
        return ((far-32)*5)/9

def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
        
class SondeT( threading.Thread) : # url du site
    address = 0x76
    address1 = 0x76
    address2 = 0x77
    idSonde= ""         #id de la sonde, dans notre cas ça correspond à l'adresse i2c de la sonde
    isActivate = False  #sert à indiquer au thread de se fermer
    rateBetweenData = 1 #en sec
    # Initialize I2C bus
    bus = smbus2.SMBus(1)

    # Load calibration parameters
    calibration_params = bme280.load_calibration_params(bus, address1)
        
    def __init__(self, sonde, address) :
        super(SondeT, self).__init__()
        self.idSonde = sonde
        self._stop_event = threading.Event()
        calibration_params = bme280.load_calibration_params(self.bus, address)

    def close(self):
        return self.isActivate

    def run(self) :
            
        print('Program begin')
        while True :
            try:
                if self.isActivate:
                    # Extract temperature, pressure, and humidity
                    print("boucle")
                    p = self.realPrelevement()
                    date = str(datetime.datetime.now())

                    r = requests.post(baseUrl + '/re', json={
                        "temperature": p.temperature,
                        "humidite": p.humidite,
                        "sonde_id": str(self.idSonde),
                        "date": date
                    })
                    print(f"Status Code: {r.status_code}, Response: {r.json()}")
                time.sleep(self.rateBetweenData)

            except KeyboardInterrupt:
                print('Program stopped')
                self.close()
                break
            except Exception as e:
                print('An unexpected error occurred:', str(e))
                self.close()
                break
        
        return "############################################Désactivation de la sonde " + self.idSonde
    
    def fakePrelevement(self) :
        listT = []
        listH = []
        n = 5
        i = 0
        rate = 0.5

        while i < n:
            try:
                listT.append(random.randint(-5, 40))
                listH.append(random.randint(0, 100))
                i += 1
                print(i)
                time.sleep(rate)

            except KeyboardInterrupt:
                print('Program stopped')
                self.stop()
                break
            except Exception as e:
                print('An unexpected error occurred:', str(e))
                self.stop()
                break
        
        print(prelevement.Prelevement(statistics.mean(listT), statistics.mean(listH)))
        return prelevement.Prelevement(statistics.mean(listT), statistics.mean(listH))
    
    def realPrelevement(self) :
        
        listT = []
        listH = []
        n = 5
        i = 0
        rate = 0.5

        while i < n:
            try:
                # Read sensor data
                data = bme280.sample(self.bus, self.address1, self.calibration_params)
                listT.append(data.temperature)
                listH.append(data.humidity)
                i += 1
                print(i)
                time.sleep(rate)

            except KeyboardInterrupt:
                print('Program stopped')
                self.close()
                break
            except Exception as e:
                print('An unexpected error occurred:', str(e))
                self.close()
                break
        return prelevement.Prelevement(statistics.mean(listT), statistics.mean(listH))
