sinif = {110:"Ali",225:"Ayşe",113:"Mehmet"}
print(sinif)







sayi = input("iki basamaklı sayı giriniz:")

d_birler = {1:"bir",2:"iki",3:"üç",4:"dört",5:"beş",6:"altı",7:"yedi",8:"sekiz",9:"dokuz",0:""}
d_onlar = {1:"on",2:"yirmi",3:"otuz",4:"kırk",5:"elli",6:"altmış",7:"yetmiş",8:"seksen",9:"doksan",0:""}

onlar = int(sayi[0])
birler = int(sayi[1])

print(d_onlar[onlar],d_birler[birler])