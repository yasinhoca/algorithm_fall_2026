dizi = [3,2,0,2,5,7,8,4,9]
print(dizi)

cift = list(filter(lambda x:x%2==0,dizi))
print(cift)

tek = list(filter(lambda x:x%2==1,dizi))
print(tek)

b = list(filter(lambda x:x>1 and x<5,dizi))
print(b)

c = list(filter(lambda x:x>10,dizi))
print(c)

liste=[25,30,78,21,34,56,22,77,84]
d = list(filter(lambda x:x%7==0 or x%11==0,liste))
print(d)