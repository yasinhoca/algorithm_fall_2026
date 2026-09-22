a = int(input("a sayısını gir ="))
b = int(input("b sayısını gir ="))
c = int(input("c sayısını gir ="))

if a>=b and a>=c:
    print("En büyük a = ",a)
elif b>=a and b>=c:
    print("En büyük b = ",b)
else:
    print("En büyük c = ",c)

