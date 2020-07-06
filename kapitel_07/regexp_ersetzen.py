import re

tx = "Haus und Maus und Laus"
print(tx)

erg = re.sub("Maus", "X", tx)
print("1.", erg)

erg = re.sub("[H|M]aus", "X", tx)
print("2.", erg)

erg = re.sub("[L-M]aus", "X", tx)
print("3.", erg)

erg = re.sub("[^L-M]aus", "X", tx)
print("4.", erg)

erg = re.sub(".aus", "X", tx)
print("5.", erg)

erg = re.sub("^.aus", "X", tx)
print("6.", erg)

erg = re.sub(".aus$", "X", tx)
print("7.", erg)