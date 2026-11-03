# kullanıcıdan ismini alıp tahmin edelim
import random as r

def randomStringUret(isim):
    s = ""
    for i in range(len(isim)):
        s += chr(r.randint(97, 122))
    return s






isim = input("İsminizi küçük harfle giriniz = ")
sayac=0
while True:
    sayac+=1
    rast = randomStringUret(isim)
    print(sayac,". deneme =",rast)
    if rast==isim:
        print("Bulundu tebrikler!",sayac)
        break