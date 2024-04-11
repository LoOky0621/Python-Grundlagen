#Übung Seite 39 Teil 2

#Berechnung der Steuer mit 18%

print("Geben Sie Ihr Gehalt in Euro ein:")      #Aufforderung zur Eingabe

i = input()                                     #Eingabe wird eine Variabel i zugewiesn
z = float(i)                                    #Variabel i wird in Fließzahl Zahl umgewandelt

s = (z*18)/100                                  #Berechung von der eingegeben Zahl und zuweisung zu s
s = float(s)                                    #S wird in Fließzahl umgewandelt

print("Es ergibt sich eine Stuer von", s,"Euro")#Ausgabe der Variablen