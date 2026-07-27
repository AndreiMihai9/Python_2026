def prim(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

n = int(input("Introdu un numar: "))
if prim(n):
    print(n, "este prim")
else:
    print(n, "nu este prim")