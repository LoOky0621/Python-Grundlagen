# Funktionen mit str

# Beispiel
test = "Das ist ein Beispielsatz"
print("Text:", test)

# Anzahl Suchtexte
such = "ei"
anz = test.count(such)
print("count: Der String", such, "kommt", anz, "Mal vor")

# Erste Position des Suchtextes
anfpos = test.find(such)
print("find 1: Zum ersten Mal an Position", anfpos)

# Weitere Position des Suchtextes
nextpos = test.find(such, anfpos+1)
print("find 2: Ein weiteres Mal an der Position", nextpos)

# Letzte Position des Suchtextes
endpos = test.rfind(such)                                           # Falls der der gesuchte Text nicht vorkommt gibt die funktion "rfind unf find" den wert -1 zurück

print("rfind: Zum letzten Mal an der Position", endpos)

# Suchtext nicht gefunden
such = "am"
pos = test.find(such)

if pos == -1:
    print("find 3:", such, "wird nicht gefunden")
else:
    print("find 3:", such, "an Position", pos, "gefunden")    

# Suchtext nicht gefunden
such = "am"
test = test.replace("ist", "war")
print("replace:", test)
