from sonde import *
import threading
import time
import requests
import json

baseUrl = "http://10.121.128.165:5000/"

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
i = 0
for d in data:
      print("sonde : ", d)
      s = SondeT(d["id"], 0x76)
      list.append(s)

#Activation de toutes les sondes au lancement
for t in list :
      t.start()
#      r2 = requests.put(baseUrl +'/sonde/' + t.idSonde, json = {
#                    "activation" : True 
#                })
print(list, " ejlipjgrgrjirtghinoiohnvijhpfdonpjjjjjgd")
#boucle principale de gestion des sondes 
while len(list) > 0 :
    try :
        for t in list :
                print("Boucle manager")
                if t.isActivate == False:
                    print("alive")
                    #Vérifie si la sonde est désactivée alors qu'elle est active sur la table Sonde dans la BDD
                    if t.isActivate == False and is_activate(t.idSonde) :
                        t.isActivate = True
                        print("Relance la sonde")
                else :
                    #Vérifie si la sonde est désactivée en consultant la table Sonde dans la BDD
                    if is_activate(t.idSonde) == False:
                        t.isActivate = False
                        print("La sonde est inactive")
        time.sleep(1)
    except Exception as e:
                print('An unexpected error occurred:', str(e))
                break
