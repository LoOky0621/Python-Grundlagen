#Kopfrechnen Spiel Teil9
#Erweiterung mit if-elif-else

import random

#Zufallsgenerator initialisieren
random.seed()               #Die Funktion seed() führt dazu, dass der Zufallsgenerator mit der aktuellen Systemzeit
                            #Initialisiert wird, Andernfalls könnte es passieren, das anstelle einer zufälligen Auswahl 
                            #Immer wieder die gleiche Zahlen geliefert wird.

                        

#Zufallswete und Berechnung

a = random.randint(1, 10)   #variable a wird eine zufällige Zahl zugewiesen
b = random.randint(1, 10)   #variable b wird eine zufällige Zahl zugewiesen
                            #Die Funktion randint() des Moduls random liefert eine ganze Zufallszahl im
                            #Eingabebereich von 1 bis 10
#Berechnung

c = a + b                   #Formel zu berechung von Addition
print("Die Aufgabe:", a, "+", b)    #Zeigt die Aufgabe an

#Eingabe

print("Bitte geben sie Ihr Ergebniss ein:")
z = int(input())

if z == c:

    print(z, "ist richtig")

elif z < 0 or z > 100:

    print(z, "ist ganz falsch")

elif c-1 <= z <= c+1:

    print(z, "ist ganz nahe dran")       

else:

    print(z, "ist falsch")

print("Das Ergebnis:", c)           #Zeigt das Ergebinis an