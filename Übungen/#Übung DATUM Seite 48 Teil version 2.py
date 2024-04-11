#Übung DATUM Seite 48 Teil version 2
#Überprüfung auf richtigen Tag durch Eingabe

print("Tag des Datums eingeben:")

t = input()                             #Eingabe aufforderung
tag = int(t)                            #Umwandlung des wertes in eine ganze Zahl

print("Monat des Datums eingeben:")

m = input()
monat = int(m)

print("Jahr des Datums eingeben:")

j = input()
jahr = float(j)

if tag < 1 or tag > 31:                 #Trifft zu, wenn der Tag 0 oder über 31 ist

    print("Falsche Datum")

elif monat < 1 or monat > 12:           #Trifft zu, wenn der Monat 0 oder über 31 ist

    print("Flasches Datum")      

elif monat == 2:                        #Trifft zu, wenn der Monat der Februar ist

    if jahr%4 != 0:                     #Trifft zu, wenn das Jahr kein Schaltjahr ist
            
        if tag < 1 or tag > 28:         #Trifft zu, wenn der Tag auserhalb Februar liegt (28Tage)

            print("Flasches Datum")

        else:                           #Trifft zu, wenn der Tag innerhalb Februar liegt

            print("Letzter Tag: 28")

    else:                               #Trifft zu, wenn das Jahr ein Schaltjahr ist
        
        if tag < 1 or tag > 29:         #Trifft zu, wenn der Tag auserhalb Februar liegt (29Tage)

            print("Flasches Datum")

        else:                           #Trifft zu, wenn der Tag innerhalb Februar liegt

            print("Letzter Tag: 29")
        
elif monat == 4 or monat == 6 or monat == 9 or monat == 11: #Trifft zu, wenn der Monat: April, 
                                                            #Juli, September oder November ist

        if tag < 1 or tag > 30:         #Trifft zu, wenn der Tag 0 oder über 30 ist

            print("Flasches Datum")

        else:                           #Trifft zu, wenn der Tag zwischen 1 - 30 ist

            print("Letzter Tag: 30")

else:                                   #Trifft für alle übrigen Monate zu

        if tag < 1 or tag > 31:         #Trifft zu, wenn der Tag= 0 oder über 31 ist 

            print("Flasches Datum")

        else:                           #Trifft zu, wenn der Tag zwischen 1- 31 ist

            print("Letzter Tag: 31")