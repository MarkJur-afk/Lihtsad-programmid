#task 2

from math import *
a = 3 + 8 / (4 - 2) * 4 #esimene variant
b = 3 + 8 / 4 - (2 * 4) #sin on teine variant, esimene on verang 2 * 4 ja pärast kõik 
c = 3 + (8 / 4) - 2 * 4 #
d = (3 + 8) / 4 - 2 * 4
f = (3 + 8 / 4) - 2 * 4
print(a, b, c, d, f)

#task 3
#Внутри квадрата находится круг. Радиус круга равен R.
#Найдите и выведите на экран площадь квадрата, периметр квадрата, площадь круга и длину окружности круга.
from math import *
try:   
    r=float(input("Mis on raadius?: "))
    Sr=round((2*r)**2,2)
    So=round(pi*r**2,2)
    Pr=round(8*r,2)
    Prin=round(2*pi*r,2)
    print(f"vastus: Ruudu pindala: {Sr}, nringi pindala on: {So}, ruudu umberemott: {Pr}, Ringi umbermoot on: {Prin}. ")
    print()
except:
    print("Sisesta ujukomaarv!")


