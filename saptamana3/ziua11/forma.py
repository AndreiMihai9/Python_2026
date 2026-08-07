PI = 3.14159

class Dreptunghi:
    def __init__(self, l, L):
        self.l = l
        self.L = L

    def arie(self):
        return self.l * self.L

    def perimetru(self):
        return 2 * (self.l + self.L)

    def este_patrat(self):
        return self.l == self.L

    def __str__(self):
        return "Dreptunghi " + str(self.l) + "x" + str(self.L)

class Cerc:
    def __init__(self, r):
        self.r = r

    def arie(self):
        return PI * self.r * self.r

    def perimetru(self):
        return 2 * PI * self.r

    def __str__(self):
        return "Cerc cu raza " + str(self.r)


if __name__ == "__main__":
    lst_f = [Dreptunghi(3, 5), Dreptunghi(4, 4), Cerc(2), Cerc(1.5)]

    for f in lst_f:
        print(f)
        print("  arie      =", round(f.arie(), 2))
        print("  perimetru =", round(f.perimetru(), 2))

    f_max = lst_f[0]
    for f in lst_f:
        if f.arie() > f_max.arie():
            f_max = f
    print("\nAria maxima:", f_max, "->", round(f_max.arie(), 2))