from math import sqrt
from itertools import count, islice

n = int(input("Bitte Zahl eingeben: "))

def isPrime(n):
    if n < 2:
        return "Keine Primzahl"

    for number in islice(count(2), int(sqrt(n) - 1)):
        if n % number == 0:
            return "Keine Primzahl"

    return "Primzahl"

print(isPrime(n))