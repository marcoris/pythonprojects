# Primzahltest
z = 200

def prim(x):
    if abs(x) <= 1:
        return "Ist keine Primzahl"
    else:
        if x < 0:
            return prim(-x)
        else:
            return pr(2, x)

def pr(x, y):
    if x >= y:
        return "Ist Primzahl"
    else:
        if y % x != 0:
            return "Ist keine Primzahl"
        else:
            return pr(x + 1, y)

print(z, prim(z))