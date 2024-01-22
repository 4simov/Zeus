
import datetime
import sys
import threading
import time
import requests
import json
import prelevement
import random
import statistics

class SondeThread( threading.Thread) :
    baseUrl = "http://10.121.128.165:5000/"   # url du site
    address1 = 0x76
    address2 = 0x77
    idSonde= ""         #id de la sonde, dans notre cas ça correspond à l'adresse i2c de la sonde
    isActivate = False  #sert à indiquer au thread de se fermer
    rateBetweenData = 1 #en sec

    def __init__(self, sonde) :
        super(SondeThread, self).__init__()
        self.idSonde = sonde
        self._stop_event = threading.Event()

    def close(self):
        return self.isActivate

    def run(self) :
        print('Program begin')
        while True :
            try:
                if self.isActivate:
                    # Extract temperature, pressure, and humidity
                    print("boucle")
                    p = self.fakePrelevement()
                    date = str(datetime.datetime.now())

                    r = requests.post(self.baseUrl + '/re', json={
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
        return prelevement.Prelevement(statistics.mean(listT), statistics.mean(listH))
    
    def realPrelevement() :
        return prelevement.Prelevement()

