import random

print("=== Ghiceste numarul ===")

print("1. Usor (1-50)")
print("2. Mediu (1-100)")
print("3. Greu (1-1000)")

n = input("Alege nivelul: ")

if n == "1":
    m = 50
    t = 8
elif n == "3":
    m = 1000
    t = 12
else:
    m = 100
    t = 10

s = random.randint(1, m)
i = 0
b = False

print(f"\nAm ales un numar intre 1 si {m}. Ai {t} incercari.")

while i < t:
    g = int(input(f"Incercarea {i + 1}/{t}: "))

    if g < 1 or g > m:
        print(f"Numarul trebuie sa fie intre 1 si {m}.")
        continue

    i += 1

    if g < s:
        print("Prea mic!")
    elif g > s:
        print("Prea mare!")
    else:
        print(f"Felicitari! Ai ghicit din {i} incercari.")
        b = True
        break

if not b:
    print(f"Ai ramas fara incercari. Numarul era {s}.")