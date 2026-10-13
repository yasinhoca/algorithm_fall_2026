import random as r

rast = r.randint(0,100)
sayac = 0;





while True:
    sayi = int(input("0 ile 100 arasında bir sayı tahmin et="))
    sayac += 1
    print(sayac,". deneme")
    if sayi==rast :
        print("Tebrikler")
        break
    elif sayi>rast:
        print("Daha küçük bir sayı dene!")
    else:
        print("Daha büyük bir sayı dene!")

