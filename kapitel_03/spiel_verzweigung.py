# Modul random importieren
import random

# Zufallsgenerator initialisieren
random.seed()

# Zufallswerte und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe:", a, "+", b)

# Eingabe
print("Bitte eine Zahl eingeben")
z = input()
zahl = int(z)

# Verzweigung
if zahl == c:
    print(zahl,"ist richtig")
else:
    print(zahl,"ist falsch")
    print("Ergebnis:", c)