# ikili şekilde işlem yaparak azaltır
from functools import reduce

dizi = [2,5,4,1,0,9]
print(dizi)

toplam = reduce(lambda x,y:x+y,dizi)
print(toplam)

azaltma = reduce(lambda x,y:x-y,dizi)
print(azaltma)

a2 = reduce(lambda x,y:x-y if x>=y else y-x,dizi)
print(a2)

a3 = reduce(lambda x,y:x-y if x%2==0 else y+x,dizi)
print(a3)

enbuyuk = reduce(lambda x,y:x if x>=y else y,dizi)
print(enbuyuk)

#dizi = [2,5,4,1,0,9]
a4 = reduce(lambda x,y:(x*y)-1 if x%3==0 or x%4==0 else (y+x)+1,dizi)
print(a4)