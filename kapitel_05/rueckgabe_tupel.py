import math

def kreis(radius):
    flaeche = math.pi * radius * radius
    umfang = 2 * math.pi * radius

    return flaeche, umfang

f, u = kreis(3)
print("Fläche:", f)
print("Umfang:", u)