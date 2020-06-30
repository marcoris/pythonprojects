# Modul math
import math

# Trigonometrische Funktionen
x = 30
xbm = math.radians(x)
xgr = math.degrees(x)

print("Grad")
print("---------------")
print("Sinus", x, "Grad:", math.sin(xbm))
print("Cosinus", x, "Grad:", math.cos(xbm))
print("Tangens", x, "Grad:", math.tan(xbm))

print("Bogenmass")
print("---------------")
print("Sinus", x, ":", math.sin(xgr))
print("Cosinus", x, ":", math.cos(xgr))
print("Tangens", x, ":", math.tan(xgr))