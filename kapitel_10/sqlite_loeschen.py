import sqlite3

def ausgabe():
    # SQL Abfrage
    sql = "SELECT * FROM personen"
    cursor.execute(sql)
    for dsatz in cursor:
        print(dsatz[0], dsatz[1], dsatz[2], dsatz[3], dsatz[4])
    print()

# Verbindung, Cursor
connection = sqlite3.connect("firma.db")
cursor = connection.cursor()

#Vorher
print("Vorher")
ausgabe()

# Datensatz entfernen
sql = "DELETE FROM personen WHERE personalnummer = 8339"
cursor.execute(sql)
connection.commit()

# Nachher
print("Nachher")
ausgabe()

connection.close()