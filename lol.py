print("Tere!")
print("Kes sa oled?")
input("Tere, minu nimi on")
import math

a,b,c = input("Sisesta arvu väärtused a, b and c: ")
a = int(a)
b = int(b)
c = int(c)
d = pow(b,2)-4*a*c # discriminant

if d < 0:
    print ("This equation has no real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c))/2*a
    print ("This equation has one solutions: "), x
else:
    x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
    x2 = (-b-math.sqrt(b**2-4*a*c))/2*a
    print ("This equation has two solutions: ", x1, " and"), x2
      
      




