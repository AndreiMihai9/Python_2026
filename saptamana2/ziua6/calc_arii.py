import math

def arie_patrat(lat):
    return lat * lat

def arie_dreptunghi(lng, lat):
    return lng * lat

def arie_cerc(raza):
    return math.pi * raza * raza

def arie_triunghi(bz, inl):
    return (bz * inl) / 2

print("1. Patrat")
print("2. Dreptunghi")
print("3. Cerc")
print("4. Triunghi")
opt = input("Alege forma (1-4): ")

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
else:
    print("Optiune invalida.")