from datetime import datetime, date

ZILE = ["luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"]
LUNI = ["", "ianuarie", "februarie", "martie", "aprilie", "mai", "iunie",
        "iulie", "august", "septembrie", "octombrie", "noiembrie", "decembrie"]

acum = datetime.now()
azi = acum.date()

print("Data si ora:", acum.strftime("%d-%m-%Y %H:%M:%S"))
print(f"Azi este {ZILE[azi.weekday()]}, {azi.day} {LUNI[azi.month]} {azi.year}")

an_nou = date(azi.year + 1, 1, 1)
zr = (an_nou - azi).days
print(f"\nPana la 1 ianuarie {azi.year + 1} mai sunt {zr} zile.")

print("\nIntrodu data nasterii:")
zi = input("Ziua (1-31): ").strip()
ln = input("Luna (1-12): ").strip()
an = input("Anul: ").strip()

if not (zi.isdigit() and ln.isdigit() and an.isdigit()):
    print("Trebuie sa introduci doar cifre.")
else:
    zi = int(zi)
    ln = int(ln)
    an = int(an)

    if ln < 1 or ln > 12 or zi < 1 or zi > 31 or an < 1900 or an > azi.year:
        print("Data introdusa nu este valida.")
    else:
        nast = date(an, ln, zi)
        zt = (azi - nast).days
        print(f"\nTe-ai nascut intr-o zi de {ZILE[nast.weekday()]}.")
        print(f"Ai trait {zt} zile, adica aproximativ {zt // 365} ani.")
        print(f"Sunt {zt * 24} ore si {zt // 7} saptamani.")