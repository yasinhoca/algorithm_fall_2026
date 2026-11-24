# Decorators
# Python'da decorator'lar, argüman olarak fonksiyon alıp,
# sonuçta yine fonksiyon döndüren fonksiyonlara denir.

def linkYap(f):
    def yaz():
        return "<a href='http://www." + f() + ".com'>Link</a>"
    return yaz


def adres():
    return "google"

a = linkYap(adres)
print(a())

@linkYap    #fonksiyonu decoratora bağla
def adr():
    return "python"

