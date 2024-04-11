#Übung Seite 39 Teil 1

#Berechnung von Inch in cm

print("Bitte geben Sie den Inch-Wert ein:")     #Aufforderung zur Eingabe

i = input()                                     #Eingabe wird eine Variabel i zugewiesn
z = int(i)                                      #Variabel i wird in ganze Zahl umgewandelt

s = 2.54 * z                                    #Berechung von der eingegeben Zahl und zuweisung zu s
s = float(s)                                    #S wird in Fließzahl umgewandelt

print(z, "Inch sind:", s,"cm")                  #Ausgabe von beiden Variablen