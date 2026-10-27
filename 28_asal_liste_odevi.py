import random as r

boyut = int(input("Kaç elemanlı bir liste istiyorsun? ="))

baslangic = int(input("Başlangıç sayısı = "))
bitis = int(input("Bitis sayısı = "))

asal_liste = []

for i in range(baslangic,bitis):
    bolen_sayac = 0
    for j in range(2,i):
        if i%j==0:
            bolen_sayac +=1
    if(bolen_sayac==0):
        asal_liste.append(i)

print(asal_liste)

liste = []

for i in range(boyut):
    liste.append(asal_liste[r.randint(0,len(asal_liste)-1)])

print(liste)