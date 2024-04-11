# Funktionen und Operationen Teil1

# Originalliste
fr = ["Paris", "Lyon", "Marseile", "Bordeaux"]
print("Orginal:")
print(fr)

# Ersetzen eines Elements durch ein Element
fr[2] = "Lens"
print("Element ersetzt:")
print(fr)

# Ersetzen eines Teilbereiches durch eine Liste
fr[1:3] = ["Nancy", "Metz", "Gap"]
print("Teil ersetzt:")
print(fr)

# Entnehmen eines Teilbereiches
del fr[3:]
print("Teil entnommen:")
print(fr)

# Ersetzen eines Elements durch eine Liste
fr[0] = ["Paris-Nord", "Paris-Süd"]
print("Element durch Liste ersetzt:")
print(fr)