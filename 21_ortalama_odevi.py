import math

a = int(input("Başlangıç ="))
b = int(input("Bitiş ="))

toplam = 0

for i in range(a,b):
    toplam +=i

print("Toplam =",toplam)
o = toplam/(b-a)
print("Ortalama = ",o)

#harmonik
#önce 1/xi toplamını yapalım
terstoplam = 0
for i in range(a,b):
    terstoplam += (1/i)

hort=1/terstoplam
print("Harmonik ortalama = ",hort)

#geometrik ortalamada ilk önce çarpımları bulalım
carpimlar=1
for i in range(a,b):
    carpimlar *= i

geort = math.pow(carpimlar,1/(b-a))
print("Geo ort=",geort)

#standart sapma için önce varyansı hesaplayalım
varyans = 0
for i in range(a,b):
    varyans += math.pow((i-o),2)

print("Varyans =",varyans)
ssapma = math.sqrt(varyans/((b-a)-1))
print("Standart sapma = ",ssapma)


