print("Calculam media notelor unui elev")

n = int(input("Cate note are elevul: "))

if n <= 0:
    print("Nu sunt destule note.")
else:
    v = []
    for i in range(n):
        x = int(input(f"nota {i+1} = "))
        v.append(x)

m = 0
for x in v:
    m = m+x

print(f"Media notelor este: {m/n:.2f}")
