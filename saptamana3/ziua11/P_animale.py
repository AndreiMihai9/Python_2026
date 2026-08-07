class Animal:
    def __init__(self, nume, specie, varsta):
        self.nume = nume
        self.specie = specie
        self.varsta = varsta
        self.hranit = False

    def hraneste(self):
        self.hranit = True
        print(self.nume, "a fost hranit.")

    def __str__(self):
        if self.hranit:
            stare = "hranit"
        else:
            stare = "nehranit"
        return self.nume + " (" + self.specie + "), " + str(self.varsta) + " ani - " + stare

def afiseaza(l):
    if not l:
        print("Nu exista animale.")
        return
    print("\n--- Animale ---")
    for i in range(len(l)):
        print(str(i + 1) + ".", l[i])

def adauga(l):
    n = input("Nume: ")
    s = input("Specie: ")
    v = input("Varsta: ")

    if not v.isdigit():
        print("Varsta trebuie sa fie un numar.")
        return

    a = Animal(n, s, int(v))
    l.append(a)
    print("Adaugat:", a)

def hraneste(l):
    afiseaza(l)
    if not l:
        return

    nr = input("Numarul animalului: ")
    if not nr.isdigit() or int(nr) < 1 or int(nr) > len(l):
        print("Numar invalid.")
        return
    
    l[int(nr) - 1].hraneste()

def statistici(l):
    if not l:
        print("Nu exista animale.")
        return

    total = 0
    nehranite = 0
    for a in l:
        total = total + a.varsta
        if not a.hranit:
            nehranite = nehranite + 1

    print("\n--- Statistici ---")
    print("Numar animale:", len(l))
    print("Varsta medie :", round(total / len(l), 1), "ani")
    print("Nehranite    :", nehranite)

def main():
    l = [
        Animal("Rex", "Caine", 5),
        Animal("Mitzi", "Pisica", 3)
    ]

    while True:
        print("\n===== GESTIONARE ANIMALE =====")
        print("1. Adauga animal")
        print("2. Afiseaza animale")
        print("3. Hraneste animal")
        print("4. Statistici")
        print("0. Iesire")

        op = input("Optiune: ")

        if op == "1":
            adauga(l)
        elif op == "2":
            afiseaza(l)
        elif op == "3":
            hraneste(l)
        elif op == "4":
            statistici(l)
        elif op == "0":
            print("La revedere!")
            break
        else:
            print("Optiune invalida.")

if __name__ == "__main__":
    main()