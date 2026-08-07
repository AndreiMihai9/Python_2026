class EroareBiblioteca(Exception):
    pass

def log_actiune(f):
    # decorator: anunta ce actiune s-a executat
    def wrapper(*args, **kwargs):
        rez = f(*args, **kwargs)
        print("[log]", f.__name__, "executat")
        return rez
    return wrapper

class Publicatie:
    def __init__(self, cod, titlu, autor):
        self.cod = cod
        self.titlu = titlu
        self.autor = autor
        self.__disponibil = True        # incapsulare
        self.cititor = ""

    def este_disponibil(self):
        return self.__disponibil

    def imprumuta(self, cine):
        if not self.__disponibil:
            raise EroareBiblioteca(self.titlu + " e deja imprumutata de " + self.cititor)
        self.__disponibil = False
        self.cititor = cine

    def returneaza(self):
        if self.__disponibil:
            raise EroareBiblioteca(self.titlu + " nu e imprumutata")
        self.__disponibil = True
        self.cititor = ""

    def __str__(self):
        if self.este_disponibil():
            stare = "disponibil"
        else:
            stare = "la " + self.cititor
        return self.cod + " | " + self.titlu + " - " + self.autor + " [" + stare + "]"

class Carte(Publicatie):
    def __init__(self, cod, titlu, autor, pagini):
        super().__init__(cod, titlu, autor)
        self.pagini = pagini

    def __str__(self):
        return "[Carte] " + super().__str__() + " - " + str(self.pagini) + " pag."

class Revista(Publicatie):
    def __init__(self, cod, titlu, autor, numar):
        super().__init__(cod, titlu, autor)
        self.numar = numar

    def __str__(self):
        return "[Revista] " + super().__str__() + " - nr. " + str(self.numar)

class Biblioteca:
    def __init__(self):
        self.lst = []

    def cauta_cod(self, cod):
        for p in self.lst:
            if p.cod == cod:
                return p
        raise EroareBiblioteca("Nu exista publicatia " + cod)

    def cauta_text(self, text):
        for p in self.lst:
            if text.lower() in p.titlu.lower() or text.lower() in p.autor.lower():
                yield p

    @log_actiune
    def imprumuta(self, cod, cine):
        self.cauta_cod(cod).imprumuta(cine)

    @log_actiune
    def returneaza(self, cod):
        self.cauta_cod(cod).returneaza()

    def statistici(self):
        imprumutate = 0
        for p in self.lst:
            if not p.este_disponibil():
                imprumutate = imprumutate + 1

        print("\n--- Statistici ---")
        print("Total       :", len(self.lst))
        print("Imprumutate :", imprumutate)
        print("Disponibile :", len(self.lst) - imprumutate)

def main():
    b = Biblioteca()
    b.lst = [
        Carte("C1", "Ion", "Liviu Rebreanu", 480),
        Carte("C2", "Morometii", "Marin Preda", 560),
        Revista("R1", "Stiinta si Tehnica", "Redactia", 3)
    ]

    while True:
        print("\n===== BIBLIOTECA VIRTUALA =====")
        print("1. Afiseaza toate")
        print("2. Imprumuta")
        print("3. Returneaza")
        print("4. Cauta")
        print("5. Statistici")
        print("0. Iesire")

        op = input("Optiune: ")

        if op == "0":
            print("La revedere!")
            break

        try:
            if op == "1":
                for p in b.lst:
                    print(" ", p)

            elif op == "2":
                b.imprumuta(input("Cod: "), input("Cititor: "))
                print("Imprumut inregistrat.")

            elif op == "3":
                b.returneaza(input("Cod: "))
                print("Returnare inregistrata.")

            elif op == "4":
                gasite = list(b.cauta_text(input("Cauta: ")))
                if not gasite:
                    print("Niciun rezultat.")
                for p in gasite:
                    print(" ", p)

            elif op == "5":
                b.statistici()

            else:
                print("Optiune invalida.")

        except EroareBiblioteca as e:
            print("Eroare:", e)

if __name__ == "__main__":
    main()