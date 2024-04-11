# Zerlegen von Texten

# Beispiel

test = "Das ist ein Beispielsatz"
print("Text:", test)

# Beginn, Ende  
if test.startswith("Das"):                  # startswith liefern immer True oder False aus, 
                                            # daher kann der Rückgabewert direkt als Bedingung genutzt werden 
    print("Text beginnt mit Das")
if not test.endswith("Das"):                    
    print("Text endet nicht mit Das")

# Zerlegung
teile = test.partition("ei") 
print("vor der 1. Teilung:", teile[0])
print("hinter der 1. Teilung:", teile[2])

teile = test.rpartition("ei")
print("vor der 2. Teilung:", teile[0])
print("hinter der 2. Teilung:", teile[2])

#Zerlegung in Liste
wliste = test.split()
for i in range(0, 3):
    print("Element:", i, wliste[i])