#Simplifie la transmission des résultats de la sonde 
class Prelevement() :
    temperature = 0
    humidite = 0
    
    def __init__(self) :
        self.temperature = 0
        self.humidite = 0

    def __init__(self, t, h) :
        self.temperature = t
        self.h = h

    def add(self, prelevement) :
        self.temperature = prelevement.temperature
        self.humidite = prelevement.humidite
