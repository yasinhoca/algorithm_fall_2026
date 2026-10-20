#1-49 arasında 6 rakam seçen algoritma
#rakamlar iki kere seçilmeyecek
import random

l = []

for i in range(1,50):
    l.append(i)

print(l)

random.shuffle(l)
print(l)

for i in range(0,6):
    print(l[i])