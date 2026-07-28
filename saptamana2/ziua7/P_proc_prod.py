from functools import reduce

prod = [
    {"nume": "lapte",    "pret": 6.5,  "cant": 3},
    {"nume": "paine",    "pret": 4.0,  "cant": 2},
    {"nume": "cascaval", "pret": 25.0, "cant": 1},
    {"nume": "apa",      "pret": 3.0,  "cant": 6},
    {"nume": "cafea",    "pret": 32.0, "cant": 1},
]

# map / comprehension: preturi reduse cu 10%
pr = [round(p["pret"] * 0.9, 2) for p in prod]
print("Preturi -10%:", pr)

#produse cu pret sub prag
prag = 10
ieft = list(filter(lambda p: p["pret"] < prag, prod))
print(f"Sub {prag} lei:", [p["nume"] for p in ieft])

#comprehension doar numele
nume = [p["nume"] for p in prod]
print("Nume:", nume)

#reduce valoarea totala a cosului
total = reduce(lambda acc, p: acc + p["pret"] * p["cant"], prod, 0)
print("Total cos:", round(total, 2), "lei")