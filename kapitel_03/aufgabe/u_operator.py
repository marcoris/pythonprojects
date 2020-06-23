# Steuerrechner
print("Bitte geben Sie Ihr Gehalt in CHF ein:")
gehalt = float(input())
print("Ledig(1) oder verheiratet(2):")
familienstand = int(input())

# Verzweigung
if gehalt > 4000 and familienstand == 1:
    steuer = gehalt * 0.26
elif gehalt <= 4000 and familienstand == 2:
    steuer = gehalt * 0.18
else:
    steuer = gehalt * 0.22

# Ausgabe
print("Es ergibt sich eine Steuer von", steuer, "CHF.")