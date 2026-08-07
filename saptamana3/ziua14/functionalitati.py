import time

def cronometru(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        rez = f(*args, **kwargs)
        t2 = time.time()
        print("[timp]", f.__name__, "a durat", round(t2 - t1, 4), "sec")
        return rez
    return wrapper


def logheaza(f):
    def wrapper(*args, **kwargs):
        print("[log] apel:", f.__name__, "cu", args)
        rez = f(*args, **kwargs)
        print("[log] rezultat:", rez)
        return rez
    return wrapper

def verifica_pozitiv(f):
    def wrapper(*args, **kwargs):
        for a in args:
            if isinstance(a, (int, float)) and a < 0:
                print("[eroare] argument negativ:", a)
                return None
        return f(*args, **kwargs)
    return wrapper

@cronometru
def suma_pana_la(n):
    s = 0
    for i in range(n):
        s = s + i
    return s

@logheaza
def inmulteste(a, b):
    return a * b


@verifica_pozitiv
def radical(x):
    return x ** 0.5

@cronometru          
@logheaza           
def putere(a, b):
    return a ** b

if __name__ == "__main__":
    print(suma_pana_la(1000000))
    print()

    inmulteste(4, 7)
    print()

    print(radical(16))
    print(radical(-9))
    print()

    putere(2, 10)