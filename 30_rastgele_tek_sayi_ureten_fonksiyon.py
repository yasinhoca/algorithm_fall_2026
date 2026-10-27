import random as r

def tekSayiUret(a,b):
    sayi = r.randint(a,b)
    if sayi%2==1:
        return sayi
    else:
        return sayi-1


print(tekSayiUret(100,200))

#kendisine gönderilen iki sayının farkını döndüren fonksiyon
def fark(a,b):
    return a-b

#mutlak değerini return eden
import math

def mutlakFark(a,b):
    return abs(a-b)

