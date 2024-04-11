#Übung Seite 48 Teil 1

#Berechnung der Steuer mit 18%, 22%, 26%
#mehr als 4000 = 26%
#2500 bis 4000 = 22%
#weniger als 2500 18%

print("Geben Sie Ihr Gehalt in Euro ein:")      #Aufforderung zur Eingabe

i = input()                                     #Eingabe wird eine Variabel i zugewiesn
z = float(i)                                    #Variabel i wird in Fließzahl Zahl umgewandelt

print("Sind sie Ledig ja oder nein?")

l = input()

if l == "ja":

    if z > 4000:

        s = (z*26)/100                                  #Berechung von der eingegeben Zahl und zuweisung zu s
        s = float(s)                                    #S wird in Fließzahl umgewandelt
        print("Es ergibt sich eine Stuer von", s,"Euro")#Ausgabe der Variablen


    else:

        s = (z*22)/100
        s = float(s)
        print("Es ergibt sich eine Stuer von", s,"Euro")    

else:

    if z > 4000:

        s = (z*22)/100                                  #Berechung von der eingegeben Zahl und zuweisung zu s
        s = float(s)                                    #S wird in Fließzahl umgewandelt
        print("Es ergibt sich eine Stuer von", s,"Euro")#Ausgabe der Variablen


    else:

        s = (z*18)/100
        s = float(s)
        print("Es ergibt sich eine Stuer von", s,"Euro")    