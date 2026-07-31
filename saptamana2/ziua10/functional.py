from functools import reduce

nr = [3, 8, 12, 5, 20, 7, 14, 1]
cuv = ["python", "cod", "functie", "lista", "set", "modul"]
prd = [
    {"nume": "laptop", "pret": 3500, "stoc": 4},
    {"nume": "mouse", "pret": 120, "stoc": 30},
    {"nume": "tastatura", "pret": 250, "stoc": 12},
    {"nume": "monitor", "pret": 900, "stoc": 0},
]

print([x * x for x in nr if x % 2 == 0])
print(list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nr))))

print({c: len(c) for c in cuv})

print([p["nume"] for p in prd if p["pret"] > 200])

print(reduce(lambda a, p: a + p["pret"] * p["stoc"], prd, 0))

for p in sorted(prd, key=lambda p: p["pret"], reverse=True):
    print(f"{p['nume']:<12} {p['pret']:>6} lei")

txt = "recapitulare saptamana doi"
frq = {c: txt.count(c) for c in set(txt) if c != " "}
print(sorted(frq.items(), key=lambda x: -x[1])[:5])

m = [[1, 2, 3], [4, 5, 6]]
print([[lin[i] for lin in m] for i in range(len(m[0]))])

cels = [-10, 0, 18, 25, 37]
print(list(map(lambda c: c * 9 / 5 + 32, cels)))

print({c[0].upper() for c in cuv})

print(max(cuv, key=lambda c: len(c)))