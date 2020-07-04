import random

random.seed()

# Ziffern
for i in range(48, 58):
    print(chr(i), end="")
print()

# Grosse Buchstaben
for i in range(65, 91):
    print(chr(i), end="")
print()

# kleine Buchstaben
for i in range(97, 123):
    print(chr(i), end="")
print()

var = "Marco Ris"
rand = random.randint(1, 25)

print()
print(var, ": Codenummern")
# Codenummern
for i in var:
    print(ord(i), end=" ")
print()
print()
print(var, ": Verschoben um", rand)

# Verschoben
for i in var:
    print(chr(ord(i) + rand), end="")