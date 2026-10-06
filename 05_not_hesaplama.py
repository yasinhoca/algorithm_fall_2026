v = int(input("Vize notu ="))
vo = int(input("Vize ödev notu ="))
f = int(input("final notu ="))

ort = v*0.375 + vo*0.125 + f*0.5
print("Ortalamanız =",ort)

if ort>=60:
    print("GEÇER")
elif ort<60 and ort>=55:
    print("ŞARTLI GEÇER")
else:
    print("KALDI")

if ort>=90 and ort<=100:
    print("Harf notunuz = AA")
elif ort>=85 and ort<90:
    print("Harf notunuz = BA")
elif ort>=75 and ort<85:
    print("Harf notunuz = BB")
elif ort>=70 and ort<75:
    print("Harf notunuz = CB")
elif ort>=60 and ort<70:
    print("Harf notunuz = CC")
elif ort>=55 and ort<60:
    print("Harf notunuz = DC")
elif ort>=50 and ort<55:
    print("Harf notunuz = DD")
else:
    print("Harf notunuz = FF")
