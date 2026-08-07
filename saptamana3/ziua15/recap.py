
class EroareVehicul(Exception):
    pass

class Vehicul:
    nr_vehicule = 0        # atribut de clasa

    def __init__(self, marca, an):
        if an < 1900 or an > 2026:
            raise EroareVehicul("An invalid: " + str(an))
        self.marca = marca
        self.an = an
        self.__km = 0                      
        Vehicul.nr_vehicule = Vehicul.nr_vehicule + 1

    def get_km(self):
        return self.__km

    def ruleaza(self, km):
        if km <= 0:
            raise EroareVehicul("Distanta trebuie sa fie pozitiva")
        self.__km = self.__km + km

    def cost_km(self):
        return 0                            

    def __str__(self):
        return self.marca + " (" + str(self.an) + ") - " + str(self.get_km()) + " km"

class Masina(Vehicul):
    def __init__(self, marca, an, consum):
        super().__init__(marca, an)
        self.consum = consum               

    def cost_km(self):
        return self.consum / 100 * 7.5     

    def __str__(self):
        return "[Masina] " + super().__str__()

class Bicicleta(Vehicul):
    def cost_km(self):
        return 0

    def __str__(self):
        return "[Bicicleta] " + super().__str__()

if __name__ == "__main__":
    l = []

    for date in [("Dacia", 2018, 6.5), ("VW", 2012, 5.8)]:
        l.append(Masina(date[0], date[1], date[2]))
    l.append(Bicicleta("Pegas", 2020))

    try:
        l.append(Masina("Test", 1800, 5))
    except EroareVehicul as e:
        print("Respins:", e)

    for v in l:
        v.ruleaza(150)
        print(v, "-> cost/km:", round(v.cost_km(), 2), "lei")

    print("Vehicule create:", Vehicul.nr_vehicule)