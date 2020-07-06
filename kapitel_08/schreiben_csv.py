import sys

# Zugriffsversuch
try:
    d = open("daten.csv", "w")
except:
    print("Dateizugriff nicht erfolgreich")
    sys.exit(0)

# Schreiben einer Liste als CSV-Datensatz
li = [36, "Marco", 1.8]
d.write(str(li[0]) + ";" + str(li[1]) + ";" + str(li[2]).replace(".", ",") + "\n")

# Schreiben einer zweidim. Liste als Datensatztabelle
dli = [[55, "Bö", 1.52], [57, "Müller", 1.95]]
for element in dli:
    d.write(str(element[0]) + ";" + str(element[1]) + ";" + str(element[2]).replace(".", ",") + "\n")

# Schliessen der Datei
d.close()