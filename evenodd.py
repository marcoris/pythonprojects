# Test ob eine Zahl gerade ist (even)
z = 119

def even(x):
    if x == 0:
        return "ist gerade"
    else:
        if x > 0:
            return odd(x-1)
        else:
            return odd(x+1)

def odd(x):
    if x == 0:
        return "ist ungerade"
    else:
        if x > 0:
            return even(x-1)
        else:
            return even(x+1)

print(z, even(z))