





dizi = [0,1,4,2,5] #dizi=[3]


def diziToplam(dizi):
    if len(dizi) == 1:
        return dizi[0]
    else:
        return dizi[0]+ diziToplam(dizi[1:])

print(diziToplam(dizi))