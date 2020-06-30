import fractions as fraction

a = 125
b = 1000

print(a, "÷", b,"=", fraction.Fraction(a, b))

c = float(a / b)
d = fraction.Fraction(c)
e = d.limit_denominator(100)

print(c, "=", fraction.Fraction(e))