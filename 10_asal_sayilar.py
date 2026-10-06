#0-100 arası asal sayıları bulduralım
for i in range(2,100):
    bolensayac = 0
    for j in range(2,i):
        if i%j==0:
            bolensayac+=1
    if bolensayac==0:
        print(i)

