dizi = [2,0,1,8,9,2]
print(dizi)

ikikat = list(map(lambda x:x*2,dizi))
print(ikikat)

besekle = list(map(lambda x:x+5,dizi))
print(besekle)

#çift sayılarda true tek sayılarda false yazdıralım
trueFalse = list(map(lambda x:True if x%2==0 else False,dizi))
print(trueFalse)

#ciftleri ikiye bolelim
ciftbol = list(map(lambda x:int(x/2) if x%2==0 else x,dizi))
print(ciftbol)

ciftbol = list(map(lambda x:int(x/2) if x>4 and x%2==0 else x+1,dizi))
print(ciftbol)

d = [2,3,0,1,6,7,8,1,0]
print(d)
#d dizisinde bulunan 2 ye ve 4 bölünen sayıları
# başka bir diziye filtreleyin
ikivedort = list(filter(lambda x:x%2==0 and x%4==0,d))
print(ikivedort)

#d dizisinde 5 ile 8 arasında bulunan sayılara 3 ekleyelim
#diğerlerinden bir çıkaralım
m = list(map(lambda x:x+3 if x>5 and x<8 else x-1,d)) #8>x>5 çalışır
print(m)

