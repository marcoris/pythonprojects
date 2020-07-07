import sys, mysql.connector, time

# Verbindung zur Datenbank auf dem Datenbankserver erstellen
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", db="firma")
except:
    print("Keine Verbindung zum Server")
    sys.exit(0)

# Execution Objekt erzeugen
cursor = connection.cursor()

# Daten auslesen
cursor.execute("SELECT * FROM personen")
result = cursor.fetchall()

cursor.close()
connection.close()

#Daten ausgeben
for data in result:
    print(time.strptime(data[4], "%d.%m.%Y"))
    print(f"{data[0]}, {data[1]}, {data[2]}, {data[3]:.2f}, {data[4]}")