x = int(input("Cate numere prime vrei sa afisezi: "))

ct = 0
nr = 2
while ct < x:
    p = True
    for d in range(2, nr ) :
        if nr % d == 0:
            p = False
            break
    if p:
        print(nr)
        ct = ct + 1
    nr = nr + 1
    