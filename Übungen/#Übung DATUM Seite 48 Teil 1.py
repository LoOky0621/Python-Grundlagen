#Übung DATUM Seite 48 Teil 1
#Eingabe überprüfung auf eingae es korekten Tages

print("Tag des Datums eingeben:")

t = input()
tag = int(t)

if tag >= 1 and tag <= 31:
    
    print("Monat des Datums eingeben:")

    m = input()
    monat = int(m)

    
    if monat >= 1 and monat <= 12:

        print("Jahr des Datums eingeben:")
        
        n = monat%2


        j = input()
        jahr = float(j)
        s= jahr%4


        if jahr >= 0:

            if monat == 2:
        
                x = 28

                if s == 0:

                    xj = x + 1

                    print("Letzter Tag:", xj)

                    if tag >= 1 and tag <=xj:

                        print("Richtiges Datum")

                    else:

                        print("Datum stimmt nicht!")    

                else:

                    print("Letzter Tag:", x)

                    if tag >= 1 and tag <=x:

                        print("Richtiges Datum")

                    else:

                        print("Datum stimmt nicht!")    

            elif n==0:

                print("Letzter Tag: 30")

                if tag >= 1 and tag <=30:

                    print("Richtiges Datum")

                else:

                    print("Datum stimmt nicht!")    

            else:

                if tag >= 1 and tag <=31:

                    print("Richtiges Datum")

                else:

                    print("Datum stimmt nicht!")    

                print("Letzter Tag: 31")     
            
    else:    

        print("Ungültige Eingabe!")

else:    

    print("Ungültige Eingabe!")