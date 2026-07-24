l = []

while True:
    print("\n1. Adauga produs")
    print("2. Sterge produs")
    print("3. Afiseaza lista")
    print("4. Iesire")

    op = input("Optiune: ")

    if op == "1":
        p = input("Produs: ")
        l.append(p)

    elif op == "2":
            p = input("Produs de sters: ")
            if p in l:
                l.remove(p)
                print("Produsul a fost scos din lista.")
            else:   
                 print("Produsul nu se afla in lista.")        
    elif op == "3":
        if len(l) == 0:
             print("Lista e goala.")
        else:
             for i, p in enumerate(l, 1):
                  print(i, p)

    elif op == "4":
        break

    else:
        print("Optiune invalida")