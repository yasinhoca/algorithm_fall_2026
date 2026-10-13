from builtins import print
from itertools import product

sayi  = [34,23,41,56,78,12,0,98,13] #diziler köşeli parantez içinde tanımlanır
#dizi indisleri 0'dan başlar
# sayi[0] -> 34
print("Dizinin ilk elemanı =",sayi[0])
print(sayi[3])
print(sayi[8]) #eleman sayısı 9, maximum indis 8
#print(sayi[9]) taşma hatası olur çünkü max indis 8'dir

print(len(sayi)) # length = len -> dizinin eleman sayısını verir

print(sayi) # dizinin tüm elemanlarını yazar

print(sayi[len(sayi)-3]) #-> 0
#print(sayi[len(sayi)]) #taşma hatası - overflow

print(sayi[0:5]) # ilk beş elemanı yaz
print(sayi[3:6])
print(sayi[:8])
print(sayi[3:])
print(sayi[-1])
print(sayi[-2])

#string dizisi
meyveler = ["elma","armut","nar","mandalina","çilek"]
print(meyveler[3])

meyveler += ["üzüm","muz","kiraz"]
print(meyveler)

meyveler.append("karpuz")
print(meyveler)

del meyveler[0] # 0 indisteki veriyi siler
print(meyveler)

meyveler.pop(0) # indis
print(meyveler)

meyveler.remove("çilek")
print(meyveler)

meyveler *=3
print(meyveler)

dizi = [0,2,1,6,8,8,9,0,3,2]
print(dizi)
dizi.sort()
print(dizi)
dizi.reverse()
print(dizi)
dizi.insert(0,5)
print(dizi)
dizi.insert(3,7)
print(dizi)

print(dizi.count(0))

dizi.clear()
print(dizi)

for i in meyveler:
    print(i)

dizi = [2,4,5,7,8,9,0,1]
for i in dizi:
    print(i)

for i in range(len(dizi)):
    print(dizi[i])

#bir dizinin içini rastgele sayılarla dolduralım
s = [] #s dizisi şu an boş
import random #rastgele sayı için import ettiğimiz kütüphane

for i in range(10):
    s.append(random.randint(0,100))

print(s)