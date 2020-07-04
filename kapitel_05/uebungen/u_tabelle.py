inch = 2.54

print(f"{'Inch':>7}{'cm':>7}")
for x in range(15, 41, 5):
    print(f"{x:7.1f}{x * inch:7.1f}")