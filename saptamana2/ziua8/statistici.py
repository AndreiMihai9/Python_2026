import csv
import os

if not os.path.exists("note.csv"):
    print("Fisierul note.csv nu exista.")
else:
    nt = {}

    with open("note.csv", "r", encoding="utf-8", newline="") as f:
        cit = csv.DictReader(f)
        for rand in cit:
            nume = rand["nume"]
            nota = float(rand["nota"])   
            if nume not in nt:
                nt[nume] = []
            nt[nume].append(nota)

    md = {}
    for nume, note in nt.items():
        md[nume] = round(sum(note) / len(note), 2)

    print("Medii:")
    for nume, m in md.items():
        print(f"  {nume:10} {m}")

    bst = ""
    mmax = -1
    for nume, m in md.items():
        if m > mmax:
            mmax = m
            bst = nume

    print(f"\nMedia cea mai mare: {bst} ({mmax})")