# Generators - Üreteçler

def uretec():
    sayi = 0
    print(sayi,". adım")
    yield sayi   # yield , return yerine kullanılır

    sayi += 1
    print(sayi, ". adım")
    yield sayi

    sayi += 1
    print(sayi, ". adım")
    yield sayi

a = uretec()

next(a)
next(a)
next(a)
# next(a)  stopiteration hatası alınır
