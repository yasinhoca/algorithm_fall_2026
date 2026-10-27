#fonksiyonlar def - define ile tanımlanır

def hosgeldin():
    print("Python'a hoşgeldin")

hosgeldin()
hosgeldin()
hosgeldin()

for i in range(100):
    hosgeldin()


#parametre alan fonksiyon
def merhaba(isim): #fonksiyon parametre alıyor
    print("merhaba",isim)

isim = input("isminizi giriniz:")
merhaba(isim) #fonksiyon çağrılmadan önce üste tanımlanmalıdır!

#sonuc döndüren fonksiyon
def carp(a,b):
    return a*b

print(carp(3,5))