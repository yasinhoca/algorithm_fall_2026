import math as m
a = int(input("a katsayısı="))
b = int(input("b katsayısı="))
c = int(input("c katsayısı="))


d = m.pow(b,2)-(4*a*c)  #delta=b*b-(4*a*c)
print("Delta =",d)

if d>0:
    print("İki kök vardır")
    k1= (-b + m.sqrt(d))/(2*a)
    print("Kök1 =",k1)
    k2 = (-b - m.sqrt(d))/(2*a)
    print("Kök2 =", k2)
elif d==0:
    print("Çakışık kök vardır")
    k = -b/(2*a)
    print("Kök =",k)
else:
    print("Kök yoktur")