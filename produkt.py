# Produkt zweier Zahlen unter Verwendung der Addition
a = 36
b = 15

def prod(x, y):
    if x == 0:
        return 0
    else:
        if x > 0:
            return prod(x - 1, y) + y
        else:
            return -prod(-x, y)

print("Das Produkt von", a, "und", b, "ist", prod(a, b))