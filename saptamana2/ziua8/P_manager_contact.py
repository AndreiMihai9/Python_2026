import json
import os

FIS = "contacte.json"

def incarca():
    """Citeste contactele din fisier, sau lista goala daca nu exista."""
    if os.path.exists(FIS):
        with open(FIS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salveaza(ct):
    with open(FIS, "w", encoding="utf-8") as f:
        json.dump(ct, f, indent=4, ensure_ascii=False)

def adauga(ct):
    nume = input("Nume: ").strip()
    tel = input("Telefon: ").strip()
    email = input("Email: ").strip()
    if nume == "":
        print("Numele nu poate fi gol.")
        return
    ct.append({"nume": nume, "telefon": tel, "email": email})
    print(f"Contact adaugat: {nume}")

def listeaza(ct):
    if len(ct) == 0:
        print("Nu exista contacte.")
        return
    print(f"\n{'#':<4}{'Nume':<20}{'Telefon':<15}{'Email'}")
    for i, c in enumerate(ct, start=1):
        print(f"{i:<4}{c['nume']:<20}{c['telefon']:<15}{c['email']}")


def cauta(ct):
    q = input("Cauta dupa nume: ").strip().lower()
    gas = [c for c in ct if q in c["nume"].lower()]
    if len(gas) == 0:
        print("Niciun rezultat.")
    else:
        for c in gas:
            print(f"  {c['nume']} | {c['telefon']} | {c['email']}")

def sterge(ct):
    listeaza(ct)
    if len(ct) == 0:
        return
    poz = input("Numarul contactului de sters: ").strip()
    if not poz.isdigit():
        print("Trebuie sa introduci un numar.")
        return
    poz = int(poz)
    if poz < 1 or poz > len(ct):
        print("Numar invalid.")
        return
    c = ct.pop(poz - 1)
    print(f"Sters: {c['nume']}")

ct = incarca()
print(f"Incarcate {len(ct)} contacte.")

while True:
    print("\n--- MANAGER CONTACTE ---")
    print("1. Adauga contact")
    print("2. Listeaza toate")
    print("3. Cauta dupa nume")
    print("4. Sterge contact")
    print("5. Salveaza si iesi")
    op = input("Optiune: ").strip()

    if op == "1":
        adauga(ct)
    elif op == "2":
        listeaza(ct)
    elif op == "3":
        cauta(ct)
    elif op == "4":
        sterge(ct)
    elif op == "5":
        salveaza(ct)
        print("Date salvate. La revedere!")
        break
    else:
        print("Optiune invalida.")