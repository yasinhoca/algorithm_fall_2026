import random as r

l = []
sayac=0

while True:
    s = r.randint(0,100)
    if s%7==0 and s!=0:
        l.append(s)
        sayac +=1
        if sayac==20:
            break

print(l)