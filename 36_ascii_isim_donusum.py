#kullanıcıdan büyük harf ingiliz alfabesi ile
#ismini alıp
#ismindeki harflerin sayısal karşığını fonksiyon ile bulalım
def asciiDonusum(isim):
    for i in isim:
        print(ord(i),"-",i)




isim = input("İsminizi giriniz")

asciiDonusum(isim)