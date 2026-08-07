class Persoana:
    def __init__(self, nume, varsta, oras):
        self.nume = nume
        self.varsta = varsta
        self.oras = oras

    def saluta(self):
        print("Salut! Ma numesc " + self.nume + " si sunt din " + self.oras + ".")

    def este_major(self):
        return self.varsta >= 18

    def aniversare(self):
        self.varsta = self.varsta + 1
        print(self.nume, "a implinit", self.varsta, "ani.")

    def __str__(self):
        return self.nume + ", " + str(self.varsta) + " ani, " + self.oras

if __name__ == "__main__":
    p = Persoana("Andrei", 21, "Sibiu")
    p2 = Persoana("Maria", 16, "Cluj")

    p.saluta()
    p2.saluta()

    print(p)          
    print(p2)

    if p2.este_major():
        print(p2.nume, "este major.")
    else:
        print(p2.nume, "este minor.")

    p.aniversare()

    lst_p = [p, p2, Persoana("Ion", 35, "Brasov")]
    print("\nPersoane majore:")
    for pers in lst_p:
        if pers.este_major():
            print(" -", pers)