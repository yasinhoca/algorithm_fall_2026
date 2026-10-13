
notlar = [20,34,67,90,12,0,100] #liste halinde int veri tutuyoruz
print(notlar)
print(notlar[0])
print(notlar[1])
print(notlar[6])
#print(notlar[7]) taşma hatası alırız
print(notlar[3],"-",notlar[4])

for i in notlar: #notlar listesindeki her elemanı sırayla i indisine atar
    print(i)

for i in range(len(notlar)): #len(notlar) kaç eleman varsa o sayıyı döndürür burada 7
    print(notlar[i])

meyveler = ["elma","armut","portakal","çilek","nar","karpuz"]
print(meyveler)
print(meyveler[2])
meyveler[2]="limon"
print(meyveler)

print(meyveler[0][3])
print(meyveler[3][1])
print(meyveler[len(meyveler[4])])
print(meyveler[len(meyveler[2])][5])  #5. meyvenin 5. harfi z

for i in meyveler:
    print(i)
