def asalMi(a):
    bolen_sayac=0
    for i in range(2,a):
        if(a%i== 0):
            bolen_sayac +=1

    if bolen_sayac==0:
        return True
    else:
        return False

print(asalMi(14))
print(asalMi(17))

