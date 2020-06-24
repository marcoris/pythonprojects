# Modul random importieren
import random

# Zufallsgenerator initialisieren
random.seed()

# Zufallswerte und Berechnung
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
print("Die Aufgabe:", a, "+", b)

# Schleife und Anzahl initialisieren
zahl = c + 1
versuch = 0

# Schleife mit while
while zahl != c:
    # Anzahl Versuche
    versuch = versuch + 1

    # Eingabe
    print("Bitte eine ganze Zahl eingeben:")
    z = input()

    # Versuch einer Umwandlung
    try:
        zahl = int(z)
    except:
        # Falls Umwandlung nicht erfolgt
        print("Sie haben keine ganze Zahl eingegeben")

        # Schleife unmittelbar fortsetzen
        continue
    
    # Verzweigung
    if zahl == c:
        print(zahl,"ist richtig")
    else:
        print(zahl,"ist falsch")

# Anzahl Versuche
print("Ergebnis:",c)
print("Anzahl Versuche:",versuch)