import sys, mysql.connector

# Verbindung zur Datenbank auf dem Datenbankserver erstellen
try:
    connection = mysql.connector.connect(host="localhost", user="root", passwd="", db="firma")
except:
    print("Keine Verbindung zum Server")
    sys.exit(0)

# Execution Objekt erzeugen
cursor = connection.cursor()

# Tabelle erzeugen
cursor.execute("CREATE TABLE IF NOT EXISTS personen"
               "(name VARCHAR(30),"
                "vorname VARCHAR(25),"
               "personalnummer INT(11) PRIMARY KEY,"
               "gehalt DOUBLE,"
               "geburtstag DATE)"
               "ENGINE=MyISAM DEFAULT CHARSET=UTF8")
connection.commit()

cursor.close()
connection.close()