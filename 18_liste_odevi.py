import random as r

l = []

for i in range(10):
    l.append(r.randint(0,100))

print(l)

tektoplam = cifttoplam = 0

for i in l:
    if i%2==0:
        cifttoplam += i
    else:
        tektoplam += i

print("TekToplam = ",tektoplam)
print("ÇiftToplam = ",cifttoplam)

