print("Introdu numere si afla care e cel mai mare")

n = int(input("Cate numere: "))
v = []
for i in range(n):
    x = int(input(f"v[{i}] = "))
    v.append(x)

m = v[0]
for nr in v:
    if nr > m:
        m == x

print(f"Numarul maxim:{m}")
