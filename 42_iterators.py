# Iterators - Yinelemeler (Tekrarlamalar)

liste = [0,3,4,7]

iterasyon = iter(liste) #iter fonksiyonu ile nesneyi tanımlıyoruz

print(next(iterasyon))  #next komutu sonraki elemanı getirir
print(next(iterasyon))
print(next(iterasyon))
print(next(iterasyon))
#print(next(iterasyon)) #stopiteration hatası

liste2 = ["ali","beril","cihan","deniz","elif","fatih"]
itr = iter(liste2)

while True:
    try :
        print(next(itr))
    except StopIteration:
        print("Listenin sonunun gelindi!")
        break


class tekSayiBul:
    def __iter__(self):
        self.sayi = 1
        return self
    def __next__(self):
        sayi = self.sayi
        self.sayi += 2
        return sayi

a = iter(tekSayiBul())

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
