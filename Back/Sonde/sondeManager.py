import threading
import time
import requests
import fakeSonde

baseUrl = "http://127.0.0.1:5000"

def is_activate(idSonde) :
        check = requests.get(baseUrl + "/sonde/" + idSonde)
        return check.json()["activate"]

print(threading.active_count())
ts1 = fakeSonde.SondeThread("118")
##ts2 = fakeSonde.SondeThread("119")

list = [ts1]
print(threading.active_count())

while True :
    try :
        for t in list :
                if t.is_alive() == False:
                    if t.isActivate == False and is_activate(t.idSonde) :
                        t.isActivate = True
                        t.start()
                        print("START")
                else :
                    print("END")
                    if is_activate(t.idSonde) == False:
                        t.isActivate = False
                        print("END")
        time.sleep(1)
    except Exception as e:
                print('An unexpected error occurred:', str(e))
                break




##ts.start()
##ts.start()