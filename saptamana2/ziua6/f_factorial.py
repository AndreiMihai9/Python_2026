def factorial(n):
    rez = 1
    for i in range(2, n + 1):
        rez *= i
    return rez


n = int(input("Introdu un numar: "))
print(n, "! =", factorial(n))