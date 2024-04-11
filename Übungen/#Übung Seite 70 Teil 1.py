#Übung Seite 70 Teil 1
#Fehlersuche in Wihle schleife

#Start Bedienung der Schleife
fehler = 1

while fehler == 1:

    #Aufforderung
    print("Bitte geben Sie ein Inch Wert ein: ")

    #Eingabe
    zahl = input()

    #Versuch der Umwandlung
    try:
        z = float(zahl)

    #Ausgabe
        print(z, "Inch sind ", z*2.54, "cm")

    #Beendet die Schleife    
        fehler = 0

    #Fehlerausgabe bei der Umwandlung
    except:
        print("Falsche Eingabe!")

#Ende des Programmes
print("Ende des Programmes")