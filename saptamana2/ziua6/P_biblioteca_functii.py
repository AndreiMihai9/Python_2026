import math

def arie_patrat(lat):
    return lat * lat

def arie_dreptunghi(lng, lat):
    return lng * lat

def arie_cerc(raza):
    return math.pi * raza * raza

def arie_triunghi(bz, inl):
    return (bz * inl) / 2

def este_prim(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def factorial(n):
    rez = 1
    for i in range(2, n + 1):
        rez *= i
    return rez

def cmmdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def converteste_baza(n, baza):
    if n == 0:
        return "0"
    cifre = "0123456789ABCDEF"
    rez = ""
    while n > 0:
        rez = cifre[n % baza] + rez
        n //= baza
    return rez

def statistici(lst):
    minim = min(lst)
    maxim = max(lst)
    media = sum(lst) / len(lst)
    return minim, maxim, media

print("Biblioteca de functii matematice")
print("1. Aria patratului")
print("2. Aria dreptunghiului")
print("3. Aria cercului")
print("4. Aria triunghiului")
print("5. Verificare numar prim")
print("6. Factorial")
print("7. CMMDC a doua numere")
print("8. Conversie in alta baza")
print("9. Statistici lista")
opt = input("Alege operatia (1-9): ")

if opt == "1":
    lat = float(input("Latura: "))
    print("Aria:", arie_patrat(lat))
elif opt == "2":
    lng = float(input("Lungimea: "))
    lat = float(input("Latimea: "))
    print("Aria:", arie_dreptunghi(lng, lat))
elif opt == "3":
    raza = float(input("Raza: "))
    print("Aria:", arie_cerc(raza))
elif opt == "4":
    bz = float(input("Baza: "))
    inl = float(input("Inaltimea: "))
    print("Aria:", arie_triunghi(bz, inl))
elif opt == "5":
    n = int(input("Numarul: "))
    print("Prim" if este_prim(n) else "Nu e prim")
elif opt == "6":
    n = int(input("Numarul: "))
    print(n, "! =", factorial(n))
elif opt == "7":
    a = int(input("Primul numar: "))
    b = int(input("Al doilea numar: "))
    print("CMMDC:", cmmdc(a, b))
elif opt == "8":
    n = int(input("Numarul: "))
    baza = int(input("Baza (2-16): "))
    print("Rezultat:", converteste_baza(n, baza))
elif opt == "9":
    text = input("Numere separate prin spatiu: ")
    lst = []
    for x in text.split():
        lst.append(float(x))
        mn, mx, md = statistici(lst)
    print("Minim:", mn, "Maxim:", mx, "Media:", md)
else:
    print("Optiune invalida.")