print("Tere!")
print("Kes sa oled?")
input("Tere, minu nimi on")
from random import *
import math
a= (randint(1, 10))
b= (randint(1, 10))
c= input("Kui palju on " + str(a) + "*" + str(b)+ "?")
if int(c) == (a*b):
    print("Tubli!")
else:
    print("Sa ei ole just kõige teravam pliiats!")
print("Järgmine tehe")
a= (randint(1, 10))
b= (randint(1, 10))
c= int(input("sisesta arv, millest võetakse ruutjuur "))
d= ("Arvuta, kui palju on " + str(a) + "**" + str(b) + "?")
print(" ruutjuur "+ str(c) + "-st on:", math.sqrt(c))

    
    