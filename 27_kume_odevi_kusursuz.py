import random
import random as r
liste = []
a = []
b = []

for i in range(100):
    liste.append(i)

print(liste)

random.shuffle(liste)
print(liste)

for i in range(20):
    a.append(liste[i])

random.shuffle(liste)
print(liste)

for i in range(20):
    b.append(liste[i])

sa = set(a)
sb = set(b)
print(sa)
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
