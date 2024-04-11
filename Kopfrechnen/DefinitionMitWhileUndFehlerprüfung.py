#Kopfrechnen Spiel Teil13
#Definition mit While und Fehlerprüfung

def aufgabe():
    a = random.randint(1, 10)   #variable a wird eine zufällige Zahl zugewiesen
    b = random.randint(1, 10)   #variable b wird eine zufällige Zahl zugewiesen
    erg = a + b                 #Die Funktion randint() des Moduls random liefert eine ganze Zufallszahl im
    print("Die Aufgabe:", a, "+", b)
    return erg                            #Eingabebereich von 1 bis 10

def kommentar(eingabezahl, ergebnis):
    if eingabezahl == ergebnis:
        print(eingabezahl, "ist richftig")
    else:
        print(eingabezahl, "ist flasch")    

import random

#Zufallsgenerator initialisieren
random.seed()               #Die Funktion seed() führt dazu, dass der Zufallsgenerator mit der aktuellen Systemzeit
                            #Initialisiert wird, Andernfalls könnte es passieren, das anstelle einer zufälligen Auswahl 
                            #Immer wieder die gleiche Zahlen geliefert wird.

#Berechnung

c = aufgabe()
zahl = c + 1
versuch = 0

while zahl != c:
    versuch = versuch + 1

    print("Bitte eine Zahl eingeben:")
    z = input()

    try: 
        zahl = int(z)
    except:
        print("Sie haben keine Zahl eingegeben")
        continue    

    kommentar(zahl, c)

print("Ergebni: ", c)
print("Anzahl Versuche: ", versuch)        