import sys, mysql.connector

# Verbindung zur Datenbank auf dem Datenbankserver erstellen
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", db="firma")
except:
    print("Keine Verbindung zum Server")
    sys.exit(0)

# Execution Objekt erzeugen
cursor = connection.cursor()

# Datensatz erzeugen
sql = "INSERT INTO personen VALUES('Maier',"\
      "'Hans', 6714, 3500, '1962-03-15')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO personen VALUES('Schmitz',"\
      "'Peter', 81343, 3500, '1962-03-15')"
cursor.execute(sql)
connection.commit()

# Datensatz erzeugen
sql = "INSERT INTO personen VALUES('Mertes',"\
      "'Julia', 2297, 3500, '1962-03-15')"
cursor.execute(sql)
connection.commit()

cursor.close()
connection.close()