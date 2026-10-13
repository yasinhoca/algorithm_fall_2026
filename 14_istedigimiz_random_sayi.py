#sıfır ile yüz arasında rastgele sayıl üretelim
#eğer ürettiğimiz sayı 60-70 aralığında olursa
#döngüyü break edelim
import random as r

#print("Ürettiğimiz random sayı = ", r.randint(0,100))
rast = 0


while True:
    rast = r.randint(0,100)
    print("Üretilen sayı = ",rast)
    if(rast>=60 and rast<=70):
        break