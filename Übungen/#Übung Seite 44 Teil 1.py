#Übung Seite 44 Teil 1

#Berechnung der Steuer mit 18% und 22%

print("Geben Sie Ihr Gehalt in Euro ein:")      #Aufforderung zur Eingabe

i = input()                                     #Eingabe wird eine Variabel i zugewiesn
z = float(i)                                    #Variabel i wird in Fließzahl Zahl umgewandelt

if z > 2500:

    s = (z*22)/100                                  #Berechung von der eingegeben Zahl und zuweisung zu s
    s = float(s)                                    #S wird in Fließzahl umgewandelt
    print("Es ergibt sich eine Stuer von", s,"Euro")#Ausgabe der Variablen

else:

    s = (z*18)/100
    s = float(s)
    print("Es ergibt sich eine Stuer von", s,"Euro")    