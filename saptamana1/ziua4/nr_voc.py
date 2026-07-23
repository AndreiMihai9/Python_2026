x = str(input("Scrie o propozitie si afla cate vocale contine aceasta: "))
s = "aeiouAEIOU"
ct = 0

for i in x:
    if i in s:
        ct = ct + 1
print(f"Propozitia contine {ct} vocale")