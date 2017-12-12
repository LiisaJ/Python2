print("Tere!")
print("Kes sa oled?")
input("Tere, minu nimi on")
import math

a = input("Sisesta a")
b = input("sisesta b")
c = input("Sisesta c")
a = int(a)
b = int(b)
c = int(c)
d = pow(b,2)-4*a*c # discriminant
print(d)
if d < 0:
    print ("Lahendid puuduvad")
else:
    x1 = round((-b+math.sqrt(b**2-4*a*c))/2*a)
    x2 =round((-b-math.sqrt(b**2-4*a*c))/2*a)
    print("Kaks lahendit: ", x1, " and", x2)
    
    
      
      




