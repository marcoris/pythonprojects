import time, threading, random

def show():
    global counter
    id = threading.get_ident()
    random.seed()
    for i in range(5):
        counter += 1
        print(i, id, counter)
        zahl = random.randint(1,10)
        time.sleep(zahl)
    return

# Hauptprogramm
id = threading.get_ident()
counter = 0
print("Start")
print(id, counter)

t1 = threading.Thread(target=show)
t1.start()
time.sleep(0.5)
t2 = threading.Thread(target=show)
t2.start()
time.sleep(10)

counter += 1
print(id, counter)
print("Ende")
