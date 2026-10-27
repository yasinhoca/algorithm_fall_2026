import random as r

a = []
b = []

for i in range(20):
    a.append(r.randint(0,100))
    b.append(r.randint(0,100))

print(a)
print(b)

sa = set(a) #aynı eleman üretebilir set edildiğinde 20'den daha az sayıda elaman oluşabilir
print(sa)
sb= set(b)
print(sb)

#A-B fark almak
fark = sa.difference(sb)
print(fark)

#AUB birleşim
birlesim = sa.union(sb)
print(birlesim)

#AnB kesişim
kesisim = sa.intersection(sb)
print(kesisim)