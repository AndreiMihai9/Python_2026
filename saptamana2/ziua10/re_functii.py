def suma_cifre(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def e_prim(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def prime_pana_la(n):
    return [x for x in range(2, n + 1) if e_prim(x)]

def inverseaza(t):
    return t[::-1]

def e_palindrom(t):
    curat = "".join(c.lower() for c in t if c.isalnum())
    return curat == curat[::-1]

def min_max_medie(lst):
    if not lst:
        return None, None, None
    return min(lst), max(lst), sum(lst) / len(lst)

def numara_vocale(t):
    voc = "aeiouAEIOU"
    return sum(1 for c in t if c in voc)

def cmmdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def cmmmc(a, b):
    return a * b // cmmdc(a, b)

def fibonacci(n):
    rez = []
    a, b = 0, 1
    for _ in range(n):
        rez.append(a)
        a, b = b, a + b
    return rez

if __name__ == "__main__":
    print("suma cifre 12345 :", suma_cifre(12345))
    print("prime <= 30      :", prime_pana_la(30))
    print("palindrom        :", e_palindrom("Ele fac cafele"))
    print("min/max/medie    :", min_max_medie([4, 8, 15, 16, 23, 42]))
    print("vocale           :", numara_vocale("programare in Python"))
    print("cmmdc / cmmmc    :", cmmdc(48, 18), cmmmc(4, 6))
    print("fibonacci 10     :", fibonacci(10))