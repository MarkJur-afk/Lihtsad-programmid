#task 2

# from cgi import print_environ_usage
# from math import *
# from string import printable
# a = 3 + 8 / (4 - 2) * 4 #esimene variant
# b = 3 + 8 / 4 - (2 * 4) #sin on teine variant, esimene on verang 2 * 4 ja pärast kõik 
# c = 3 + (8 / 4) - 2 * 4 #
# d = (3 + 8) / 4 - 2 * 4
# f = (3 + 8 / 4) - 2 * 4
# print(a, b, c, d, f)

# #task 3
# from math import *
# try:   
#     r=float(input("Mis on raadius?: "))
#     Sr=round((2*r)**2,2)
#     So=round(pi*r**2,2)
#     Pr=round(8*r,2)
#     Prin=round(2*pi*r,2)
#     print(f"vastus: Ruudu pindala: {Sr}, nringi pindala on: {So}, ruudu umberemott: {Pr}, Ringi umbermoot on: {Prin}. ")
#     print()
# except:
#     print("Sisesta ujukomaarv!")



# #Task 4
# from math import *
# r=(6378*100000) #maa diametr
# euro=2.5 #2 euro cm
# Pmaa=2*pi*r #maa umbermoot
# vastus=Pmaa/euro
# print(f"Maa katmiseks kahe euromündiga on vaja {int(vastus):,d} münte")
# print(f"Maa katmiseks kahe euromündiga on vaja {int(vastus*2):,d} euro")

# #Task 5
# a="kilo-kilo".capitalize()
# b="killadi-koll".capitalize()
# print(a*2,b,a*2,b,a*4)

#Task 6
# print("Rong see sõitis tsuhh tsuhh tsuhh,)
# print("piilupart oli rongijuht.")
# print("Rattad tegid rat tat taa,")
# print("rat tat taa ja tat tat taa.")
# print("Aga seal rongi peal,")
# print("kas sa tead, kes olid seal?")
# print()
# print("Rong see sõitis tuut tuut tuut,")
# print("piilupart oli rongijuht.")
# print("Rattad tegid kill koll koll,")
# print("kill koll koll ja kill koll kill.")

#Task 7
#Составьте программу, которая запрашивает у пользователя длины соседних сторон прямоугольника и выводит на экран периметр и площадь прямоугольника.

# try:
#     a=float(input("kolmnurga külg: "))
#     b=float(input("kolmnurga külg: "))
#     if a>0 and b>0:
#         print("arvutamine")
#         S=a*b
#         P=(a+b)*2
#         print(f"S={S}, P={P}")
#     else:
#         print("vale andmed, peavad olla surem kui 0")
        
 
# except:
#     print("Sisesta ujukomaarv!")

#Task 8

# try:
#     top=float(input("Kui palju kütust: "))
#     vahema=float(input("Läbitud vahemaa: "))
#     if top>0 and vahema>0:
#         R=round((top/vahema)*100,1)
#         print(f"Keskmine kütusekulu 100 km kohta: {R}")
#     else:
#         print("valasite liiga vähe kütust!")
# except:
#     print("numbrid peavad olema positiivsed!")

#Task 9

# from random import *
# try:
#     kesk=29.9 #km/tund
#     M=randint(1, 100) #jõuab metri minutiga
#     if M>10:
#         a=int(M*kesk)
#         print(f"{M} minutitega läbib ta saab üle {a} meetri")
#     else:
#         print("proovi uuesti!")
# except:
#     print("ilmselt on midagi valesti!")

#Task 10

# try:
#     aeg=int(input("Siselda oma aeg: "))
#     if aeg>60:
#         vastus=float(round(aeg/60,2))
#         print(vastus)
#     else:
#         print("Kirjuta rohem kui minut!")
# except:
#     print("Ei töötab!!!")