class Masina:
    nr_masini = 0
    viteza_maxima = 200

    def __init__(self, marca, model, an):
        self.marca = marca
        self.model = model
        self.an = an
        self.v = 0            
        Masina.nr_masini = Masina.nr_masini + 1  

    def accelereaza(self, val):
        self.v = self.v + val
        if self.v > Masina.viteza_maxima:
            self.v = Masina.viteza_maxima
            print("Ai atins viteza maxima!")
        print(self.model, "-> viteza:", self.v, "km/h")

    def franeaza(self, val):
        self.v = self.v - val
        if self.v < 0:
            self.v = 0
        print(self.model, "-> viteza:", self.v, "km/h")

    def vechime(self, an_curent):
        return an_curent - self.an

    def __str__(self):
        return self.marca + " " + self.model + " (" + str(self.an) + ")"


if __name__ == "__main__":
    print("Masini create pana acum:", Masina.nr_masini)

    m1 = Masina("Dacia", "Logan", 2018)
    m2 = Masina("VW", "Golf", 2012)

    print("Masini create acum:", Masina.nr_masini)

    m1.accelereaza(80)
    m1.accelereaza(150)
    m1.franeaza(100)

    print(m2, "- vechime:", m2.vechime(2026), "ani")

    print("Viteza maxima (din obiect):", m1.viteza_maxima)
    print("Viteza maxima (din clasa):", Masina.viteza_maxima)