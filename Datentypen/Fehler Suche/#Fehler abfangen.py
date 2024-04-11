#Basisprogramm 1te erweiterung
#Einfache eingabe mit Fehler abfangen

#Aufforderung
print("Bitte geben Sie eine ganze Zahl ein: ")

#Eingabe
zahl = input()

#Versuch der Umwandlung
try:
    z = int(zahl)

#Ausgabe
    print("Sie haben die Zahl", z, "richtig eingegeben")

#Fehlerausgabe bei der Umwandlung
except:
    print("Sie haben die ganze Zahl nicht richtig eingegeben")

#Ende des Programmes
print("Ende des Programmes")