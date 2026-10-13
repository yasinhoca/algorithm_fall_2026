#20 ile 30 arasında sayı alacağız
sayi = int(input("Lütfen 20 ile 30 arasında bir sayı giriniz = "))

while True:
    if(sayi>=20 and sayi<=30):
        print("Helal olsun!")
        break
    else:
        print("Hatalı giriş!")
        sayi = int(input("Lütfen 20 ile 30 arasında bir sayı giriniz = "))