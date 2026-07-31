import csv
import json
import os

with open("demo.txt", "w", encoding="utf-8") as fi:
    fi.write("prima linie\na doua linie\na treia linie\n")

with open("demo.txt", encoding="utf-8") as fi:
    lin = fi.read().splitlines()

print("linii:", len(lin), "| cuvinte:", sum(len(l.split()) for l in lin))

elevi = [
    {"nume": "Ana", "clasa": "9A", "nota": 9.5},
    {"nume": "Bogdan", "clasa": "9A", "nota": 7.0},
    {"nume": "Carmen", "clasa": "9B", "nota": 8.25},
]

with open("elevi.csv", "w", newline="", encoding="utf-8") as fi:
    scr = csv.DictWriter(fi, fieldnames=["nume", "clasa", "nota"])
    scr.writeheader()
    scr.writerows(elevi)

cit_elevi = []
with open("elevi.csv", newline="", encoding="utf-8") as fi:
    for r in csv.DictReader(fi):
        r["nota"] = float(r["nota"])   
        cit_elevi.append(r)

note = [e["nota"] for e in cit_elevi]
print(f"media generala: {sum(note) / len(note):.2f}")

clase = {}
for e in cit_elevi:
    clase.setdefault(e["clasa"], []).append(e["nota"])
for c, n in clase.items():
    print(f"{c}: media {sum(n) / len(n):.2f} ({len(n)} elevi)")

with open("elevi.json", "w", encoding="utf-8") as fi:
    json.dump(cit_elevi, fi, indent=2, ensure_ascii=False)

with open("elevi.json", encoding="utf-8") as fi:
    din_json = json.load(fi)
print("din JSON:", [e["nume"] for e in din_json])

print("elevi.csv exista:", os.path.exists("elevi.csv"))