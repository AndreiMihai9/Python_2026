import os

PRAG = 20

if not os.path.exists("text.txt"):
    print("Fisierul text.txt nu exista.")
else:
    with open("text.txt", "r", encoding="utf-8") as f:
        i = 1
        for l in f:
            print(f"{i}: {l.strip()}")
            i += 1

    with open("text.txt", "r", encoding="utf-8") as f:
        lin = f.readlines()

    lng = [l for l in lin if len(l.strip()) > PRAG]

    with open("linii_lungi.txt", "w", encoding="utf-8") as f:
        f.writelines(lng)

    print(f"\nAm scris {len(lng)} linii in linii_lungi.txt")