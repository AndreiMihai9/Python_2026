n = int(input("Cate numere: "))

l = []
for i in range(n):
    x = int(input("Numar " + str(i + 1) + ": "))
    l.append(x)

if len(l) == 0:
    print("Lista e goala.")
else:
    print("Suma:  ", sum(l))
    print("Media: ", sum(l) / len(l))
    print("Sortat:", sorted(l))

    mn = l[0]
    mx = l[0]
    for x in l:
        if x < mn:
            mn = x

    for x in l:
        if x > mx:
            mx = x

    print("Minim manual:", mn)
    print("Maxim manual:", mx)

    np = 0
    ni = 0
    for x in l:
        if x % 2 == 0:
            np = np + 1
        else:
            ni = ni + 1

    print("Pare:  ", np)
    print("Impare:", ni)