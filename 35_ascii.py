print(chr(65))
print(chr(97))
print(chr(90))
print(chr(64))
print(chr(32))
print(chr(27))

print(chr(110),chr(97),chr(122))

print(ord('A'))
print(ord("A")) #python çift tırnağıda destekler
print(ord(' '))
print(ord('Ç'))

import random
s = ""
for i in range(20): #rastgele 10 harfli string uretelim
    s += chr(random.randint(65,90))
    a = random.randint(0,2)
    if a == 0:
        s += chr(random.randint(65,90))
    elif a==1:
        s += chr(random.randint(97, 122))
    else:
        s += chr(random.randint(48, 57))
print(s)
