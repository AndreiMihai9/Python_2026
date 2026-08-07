
import random
import string

def cronometru(f):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        rez = f(*args, **kwargs)
        print("[timp]", round(time.time() - t1, 4), "sec")
        return rez
    return wrapper

def genereaza_parole(n, lung, cifre=True, simboluri=True):
    pool = string.ascii_letters
    if cifre:
        pool = pool + string.digits
    if simboluri:
        pool = pool + "!@#$%^&*"

    for i in range(n):
        p = ""
        for j in range(lung):
            p = p + random.choice(pool)
        yield p

def parole_infinit(lung):
    while True:
        yield "".join(random.choice(string.ascii_letters + string.digits)
                      for k in range(lung))

def evalueaza(p):
    scor = 0
    if len(p) >= 12:
        scor = scor + 1
    if any(c.isupper() for c in p):
        scor = scor + 1
    if any(c.isdigit() for c in p):
        scor = scor + 1
    if any(c in "!@#$%^&*" for c in p):
        scor = scor + 1

    if scor <= 1:
        return "slaba"
    if scor == 2:
        return "medie"
    if scor == 3:
        return "buna"
    return "foarte buna"

@cronometru
def salveaza(nume_fisier, gen):
    nr = 0
    with open(nume_fisier, "w", encoding="utf-8") as f:
        for p in gen:
            f.write(p + "\n")
            nr = nr + 1
    print("Salvate", nr, "parole in", nume_fisier)

def citeste_int(mesaj, minim, maxim):
    while True:
        try:
            v = int(input(mesaj))
        except ValueError:
            print("Introdu un numar intreg.")
            continue

        if v < minim or v > maxim:
            print("Valoare intre", minim, "si", maxim)
            continue
        return v

def main():
    while True:
        print("\n===== GENERATOR DE PAROLE =====")
        print("1. Genereaza parole")
        print("2. Genereaza si salveaza in fisier")
        print("3. Evalueaza o parola")
        print("4. Prima parola cu scor foarte bun")
        print("0. Iesire")

        op = input("Optiune: ")

        if op == "1":
            n = citeste_int("Cate parole: ", 1, 50)
            lung = citeste_int("Lungime: ", 4, 64)
            for p in genereaza_parole(n, lung):
                print(" ", p, "->", evalueaza(p))

        elif op == "2":
            n = citeste_int("Cate parole: ", 1, 100000)
            lung = citeste_int("Lungime: ", 4, 64)
            salveaza("parole.txt", genereaza_parole(n, lung))

        elif op == "3":
            p = input("Parola: ")
            print("Evaluare:", evalueaza(p))

        elif op == "4":
            lung = citeste_int("Lungime: ", 4, 64)
            for p in parole_infinit(lung):
                if evalueaza(p) == "foarte buna":
                    print("Gasita:", p)
                    break

        elif op == "0":
            print("La revedere!")
            break

        else:
            print("Optiune invalida.")

if __name__ == "__main__":
    main()