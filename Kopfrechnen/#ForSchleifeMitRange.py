#Kopfrechnen Spiel Teil11
#For schleife mit range

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
for i in range(1, 10):

    print("Bitte geben sie Ihr Ergebniss ein:")
    z = int(input())

    if c==z:

        print(z, "ist richitg!")
        break

    else:
        
        print(z, "ist falsch")           #Zeigt das Ergebinis an

print("Ergebni: ", c)
print("Anzahl Versuche: ", i)        