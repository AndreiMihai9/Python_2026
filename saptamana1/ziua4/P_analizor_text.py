x = input("Scrie un text: ")
x = x.lower()

if x.strip() == "":
    print("Nu ai introdus niciun text.")
    exit()

v = "aeiou"

nc = len(x)
nfs = len(x.replace(" ", ""))

cuv = x.split()
ncuv = len(cuv)

np = x.count(".") + x.count("!") + x.count("?")

tl = 0
cml = ""

for c in cuv:
    c = c.strip(".,!?;:")
    tl += len(c)
    if len(c) > len(cml):
        cml = c

med = tl / ncuv

nv = 0
ncn = 0
f = [0] * 26

for c in x:
    if "a" <= c <= "z":
        f[ord(c) - ord("a")] += 1
        if c in v:
            nv += 1
        else:
            ncn += 1

print("\n--- RAPORT ---")
print(f"Caractere (cu spatii):   {nc}")
print(f"Caractere (fara spatii): {nfs}")
print(f"Cuvinte:                 {ncuv}")
print(f"Propozitii:              {np}")
print(f"Lungime medie cuvant:    {med:.2f}")
print(f"Cel mai lung cuvant:     {cml}")
print(f"Vocale:                  {nv}")
print(f"Consoane:                {ncn}")

print("\nFrecventa literelor:")
for i in range(26):
    if f[i] > 0:
        print(f"  {chr(i + ord('a'))} apare de {f[i]} ori")