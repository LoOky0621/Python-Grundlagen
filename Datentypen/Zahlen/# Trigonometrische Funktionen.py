# Modul math

import math

# Trigonometrische Funktionen 

x = 30
# Alle Funktionen beziehen sich auf eine Angabe des Winkels im Bogenmaß
# Daher werden im nähsten Schritt wird der Winkel von Grad in Bogenmaß umgewandelt  
xbm = math.radians(x)
print("Sinus", x, "Grad:", math.sin(xbm))
print("Cosinus", x, "Grad:", math.cos(xbm))
print("Tangens", x, "Grad:", math.tan(xbm))