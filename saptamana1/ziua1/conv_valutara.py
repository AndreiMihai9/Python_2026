print("-Conversie Valutara-")

c_eur = 5.08
c_usd = 4.69
c_gbp = 5.95
r = 0
print("Valute disponibile pentru conversie: eur, usd, gbp in lei")
v = input("din ce valuta convertesti?")
s = float(input("suma: "))

if v == "eur":
    c = c_eur
elif v == "usd":
    c = c_usd
elif v == "gbp":
    c = c_gbp
else:
    c = None 
    print("Valoare necunoscuta!")

if c is not None:
    r = s * c
print(f"{s:.2f} {v} = {r:.2f} ron")
print(f"(curs folosit: 1 {v} = {c} ron)")

