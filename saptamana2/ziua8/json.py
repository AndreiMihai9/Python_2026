import csv
import json
import os

if not os.path.exists("note.csv"):
    print("Fisierul note.csv nu exista.")
else:
    nt = {}
    with open("note.csv", "r", encoding="utf-8", newline="") as f:
        cit = csv.DictReader(f)
        for rand in cit:
            nume = rand["nume"]
            if nume not in nt:
                nt[nume] = []
            nt[nume].append(float(rand["nota"]))

    md = {nume: round(sum(note) / len(note), 2) for nume, note in nt.items()}

    with open("medii.json", "w", encoding="utf-8") as f:
        json.dump(md, f, indent=4, ensure_ascii=False)
    print("Salvat in medii.json")

    with open("medii.json", "r", encoding="utf-8") as f:
        rec = json.load(f)

    print("Recitit:", rec)
    print("Identic cu originalul:", rec == md)