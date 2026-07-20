"""
Mini-proiect Ziua 1 — Calculator cu meniu

Functionalitati:
- meniu in bucla, cu iesire controlata
- 4 operatii + radacina patrata
- validare
- memorie: rezultatul anterior poate fi refolosit
- istoric al calculelor
"""
def este_numar(text):
    """Verifica daca un string poate fi transformat in float."""
    text = text.strip()
    if text.count("-") > 1 or text.count(".") > 1:
        return False
    curat = text.replace("-", "", 1).replace(".", "", 1)
    return curat.isdigit()

def citeste_numar(mesaj, rezultat_anterior):
    """
    Cere un numar utilizatorului pana cand primeste unul valid.
    Daca scrie 'm', foloseste rezultatul anterior din memorie.
    """
    while True:
        text = input(mesaj).strip()

        if text == "m":
            if rezultat_anterior is None:
                print("  ! Memoria e goala inca.")
                continue
            print(f"  > folosesc din memorie: {rezultat_anterior}")
            return rezultat_anterior

        if este_numar(text):
            return float(text)

        print("  ! Nu e un numar valid. Incearca din nou (sau 'm' pentru memorie).")

def afiseaza_meniu(rezultat_anterior):
    print("\n" + "=" * 32)
    print("        CALCULATOR")
    print("=" * 32)
    if rezultat_anterior is not None:
        print(f"  memorie (m): {rezultat_anterior}")
        print("-" * 32)
    print("  1. Adunare    2. Scadere")
    print("  3. Inmultire  4. Impartire")
    print("  5. Radacina patrata")
    print("  6. Istoric    0. Iesire")
    print("=" * 32)

def main():
    rezultat = None
    istoric = []

    while True:
        afiseaza_meniu(rezultat)
        optiune = input("Alege optiunea: ").strip()

        if optiune == "0":
            print("\nLa revedere!")
            break

        elif optiune == "6":
            if not istoric:
                print("\nIstoricul e gol.")
            else:
                print("\n--- ISTORIC ---")
                for i, linie in enumerate(istoric, start=1):
                    print(f"{i}. {linie}")
            continue

        elif optiune == "5":
            a = citeste_numar("Numar: ", rezultat)
            if a < 0:
                print("\n! Nu se poate extrage radacina dintr-un numar negativ.")
                continue
            rezultat = a ** 0.5
            operatie = f"sqrt({a}) = {rezultat:.4f}"

        elif optiune in ("1", "2", "3", "4"):
            a = citeste_numar("Primul numar:  ", rezultat)
            b = citeste_numar("Al doilea numar: ", rezultat)

            if optiune == "1":
                rezultat = a + b
                semn = "+"
            elif optiune == "2":
                rezultat = a - b
                semn = "-"
            elif optiune == "3":
                rezultat = a * b
                semn = "*"
            else:
                if b == 0:
                    print("\n! Impartire la zero. Operatia a fost anulata.")
                    continue
                rezultat = a / b
                semn = "/"

            operatie = f"{a} {semn} {b} = {rezultat:.4f}"

        else:
            print("\n! Optiune inexistenta. Alege un numar din meniu.")
            continue

        print(f"\n>>> {operatie}")
        istoric.append(operatie)


main()