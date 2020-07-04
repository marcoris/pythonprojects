# Definition der Klasse Fahrzeug
class Fahrzeug:
    geschwindigkeit = 0
    def beschleunigen(self, wert):
        self.geschwindigkeit += wert
    
    def ausgabe(self):
        print("Geschwindigkeit:", self.geschwindigkeit)

# Objekt der Klasse Fahrzeug erzeugen
opel = Fahrzeug()
volvo = Fahrzeug()

# Objektmethoden
volvo.ausgabe()
volvo.beschleunigen(20)
volvo.ausgabe()

# Objekt betrachten
opel.ausgabe()