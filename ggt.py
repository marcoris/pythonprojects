# ggT von zwei Zahlen
a = 36
b = 15

def ggt(x, y):
    if x <= 0 or y <= 0:
        return ggt(x, y)
    else:
        if x == y:
            return x
        else:
            if x > y:
                return ggt(y, x)
            else:
                return ggt(x, y-x)

print("ggT von", a, "und", b, "ist", ggt(a,b))