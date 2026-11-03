# recursive - özyinelemeli fonksiyon
# fonksiyonun kendi kendini çağırmasına recursion denir

# faktoriyel çözümü
# recursive fonksiyonlara güzel bir örnek




def faktoriyel(n):
    if n==0 or n==1:
        return 1
    else:
        return n * faktoriyel(n-1) #5 * 4 * 3 * 2 

print(faktoriyel(6))