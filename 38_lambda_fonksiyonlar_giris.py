#anonim ve lambda fonksiyonlar

def topla(a,b):
    return a+b

print(topla(3,5))



#yukarıda iki sayıyı toplayan fonksiyonun lambda tanımı
l = lambda x,y:x+y

print(l(3,5))

#kendisine gönderilen 3 sayının çarpımı
c = lambda x,y,z:x*y*z
print(c(2,3,4))

import math

kok = lambda x,y:math.pow(x,(1/y))

print(kok(75,3))
