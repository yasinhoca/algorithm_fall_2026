#girilen sayı çiftse 2 ye böl
#tek ise bir ekle ikiye böl

a = int(input("Bir sayı gir ="))

if a%2==0:
    s = a / 2
else:
    s = (a+1) / 2

print(s)