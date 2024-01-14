import threading
import time
import requests
import fakeSonde
import json

baseUrl = "http://127.0.0.1:5000"

#Consulte la table Sonde de la BDD pour savoir si la sonde est activée ou non
def is_activate(idSonde) :
        check = requests.get(baseUrl + "/sonde/" + idSonde)
        return check.json()["activate"]

#initialisation des Tables
requests.get(baseUrl + '/generate')

#Récupération des id des sondes présentent dans la table sonde
jsonSonde = requests.get(baseUrl + '/sonde')
data = json.loads(jsonSonde.content)
list = []
for d in data:
      print("sonde : ", d)
      list.append(fakeSonde.SondeThread(d["id"]))

#Activation de toutes les sondes au lancement
for t in list :
      r2 = requests.put(baseUrl +'/sonde/' + t.idSonde, json = {
                    "activation" : True 
                })

#boucle principale de gestion des sondes 
while True :
    try :
        for t in list :
                print("Boucle manager")
                if t.is_alive() == False:
                    print("alive")
                    #Vérifie si la sonde est désactivée alors qu'elle est active sur la table Sonde dans la BDD
                    if t.isActivate == False and is_activate(t.idSonde) :
                        t.isActivate = True
                        print("Relance la sonde")
                        t.start()
                else :
                    #Vérifie si la sonde est désactivée en consultant la table Sonde dans la BDD
                    if is_activate(t.idSonde) == False:
                        t.isActivate = False
                        print("La sonde est inactive")
        time.sleep(1)
    except Exception as e:
                print('An unexpected error occurred:', str(e))
                break