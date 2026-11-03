








a = 10 #global

def fonk():
    a=5 #local değişkendir yukarıdaki a ile farklı ram adreslerinde saklanır
    print(a)
    a *= 2
    #print(a)


#fonk()
#print(a)
#fonk()

################################

b = 20 #global
def ikiKati():
    global b
    print(b)
    b=5
    b *=2
    print(b)

ikiKati()
print(b)
