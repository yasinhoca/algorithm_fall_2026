a = int(input("Tabanı giriniz ="))
b = int(input("Tavanı giriniz ="))

for i in range(a,b):
    if i%3==0 and i%7==0:
        print(i)