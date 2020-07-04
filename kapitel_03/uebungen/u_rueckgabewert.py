def steuer(gehalt):
    if gehalt > 2500:
        steuerbetrag = gehalt * 0.22
    else:
        steuerbetrag = gehalt * 0.18
    
    return steuerbetrag

print("Gehalt: 1800 Euro, Steuer:", steuer(1800), "Euro")
print("Gehalt: 2200 Euro, Steuer:", steuer(2200), "Euro")
print("Gehalt: 2500 Euro, Steuer:", steuer(2500), "Euro")
print("Gehalt: 2900 Euro, Steuer:", steuer(2900), "Euro")