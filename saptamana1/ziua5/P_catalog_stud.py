
cat = {}

while True:
    print("\n1. Adauga student")
    print("2. Adauga nota")
    print("3. Afiseaza catalogul")
    print("4. Media clasei")
    print("5. Studentul cu media cea mai mare")
    print("6. Iesire")

    op = input("Optiune: ")

    if op == "1":
        nume = input("Nume: ")
        if nume in cat:
            print("Studentul exista deja.")
        else:
            cat[nume] = []
            print("Student adaugat.")

    elif op == "2":
        nume = input("Nume: ")
        if nume in cat:
            nota = float(input("Nota: "))
            if nota >= 1 and nota <= 10:
                cat[nume].append(nota)
                print("Nota adaugata.")
            else:
                print("Nota trebuie sa fie intre 1 si 10.")
        else:
            print("Studentul nu exista.")

    elif op == "3":
        if len(cat) == 0:
            print("Catalogul e gol.")
        else:
            for nume in cat:
                if len(cat[nume]) == 0:
                    print(nume, "- fara note")
                else:
                    m = sum(cat[nume]) / len(cat[nume])
                    print(nume, cat[nume], "media:", round(m, 2))

    elif op == "4":
        s = 0
        ct = 0
        for nume in cat:
            if len(cat[nume]) > 0:
                m = sum(cat[nume]) / len(cat[nume])
                s = s + m
                ct = ct + 1

        if ct == 0:
            print("Nu exista studenti cu note.")
        else:
            print("Media clasei:", round(s / ct, 2), "din", ct, "studenti")

    elif op == "5":
        mx = -1
        sm = ""
        for nume in cat:
            if len(cat[nume]) > 0:
                m = sum(cat[nume]) / len(cat[nume])
                if m > mx:
                    mx = m
                    sm = nume

        if sm == "":
            print("Nu exista studenti cu note.")
        else:
            print("Media cea mai mare:", sm, "-", round(mx, 2))

    elif op == "6":
        break

    else:
        print("Optiune invalida")