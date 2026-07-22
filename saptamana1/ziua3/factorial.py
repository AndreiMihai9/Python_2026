x = int(input("Alege un numar si afla-i factorialul: "))
r = 1
if x < 0:
    print(f"Factorialul nu e definit pentru numere negative. Alege alt numar!")
else:
    for i in range(1, x + 1):
        r = r * i
    print(f"Factorialul numarului {x} este {r}")