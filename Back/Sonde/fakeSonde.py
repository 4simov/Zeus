
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
    baseUrl = "http://127.0.0.1:5000"   # url du site
    address1 = 0x76
    address2 = 0x77
    idSonde= ""         #id de la sonde, dans notre cas ça correspond à l'adresse i2c de la sonde
    isActivate = False  #sert à indiquer au thread de se fermer
    rateBetweenData = 5 #en sec

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
                break
            except Exception as e:
                print('An unexpected error occurred:', str(e))
                break
        
        return "Désactivation de la sonde " + self.idSonde
    
    def fakePrelevement(self) :
        listT = []
        listH = []
        n = 5
        i = 0
        rate = 0.5

        while i < n:
            listT.append(random.randint(-5, 40))
            listH.append(random.randint(0, 100))
            i += 1
            print(i)
            time.sleep(rate)
        
        return prelevement.Prelevement(statistics.mean(listT), statistics.mean(listH))
    
    def realPrelevement() :
        return prelevement.Prelevement()

