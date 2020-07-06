import re

tx = "Haus und Maus und Laus"
print(tx)

erg = re.findall("Maus", tx)
print("1.", erg)

erg = re.findall("[HM]aus", tx)
print("2.", erg)

erg = re.findall("[L-M]aus", tx)
print("3.", erg)

erg = re.findall("[^L-M]aus", tx)
print("4.", erg)

erg = re.findall(".aus", tx)
print("5.", erg)

erg = re.findall("^.aus", tx)
print("6.", erg)

erg = re.findall(".aus$", tx)
print("7.", erg)