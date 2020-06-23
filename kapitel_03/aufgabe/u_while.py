# Loop ends on input = 0
wert = 1
while wert != 0:
    print("Bitte Wert in Inch angeben:")
    wert = float(input())
    print(wert,"Inch sind", wert * 2.54,"cm")