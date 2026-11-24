#dosya işlemleri

dosya = open("deneme.txt",mode="a",encoding='utf-8')
#w - write
#a - append
#r - read
#utf-8 ise Türkçe karakter desteği

for i in range(50):
    dosya.write(str(i)+". satır\n")
#\n -> new line demektir
#ikinci satırın aşağıya yazılmasını sağlar

dosya.close()


#okuma işlemi

dosya = open("deneme.txt",mode="r",encoding="utf-8")
print(dosya.read())
dosya.close()