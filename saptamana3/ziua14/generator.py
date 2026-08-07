def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a + b
        a = b
        b = temp

def numere_pare():
    n = 0
    while True:
        yield n
        n = n + 2

def citeste_linii(nf):
    with open(nf, "r", encoding="utf-8") as f:
        for linie in f:
            yield linie.strip()

if __name__ == "__main__":
    print("Fibonacci:", list(fibonacci(10)))
    g = numere_pare()
    for i in range(5):
        print(next(g), end=" ")
    print()

    patrate = (x * x for x in range(1000000))
    print("Primele 5 patrate:", [next(patrate) for i in range(5)])

    import sys
    lista = [x * x for x in range(100000)]
    gen = (x * x for x in range(100000))
    print("Lista :", sys.getsizeof(lista), "bytes")
    print("Gener.:", sys.getsizeof(gen), "bytes")

    print("Suma primelor 20 Fibonacci:", sum(fibonacci(20)))

    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("linia 1\nlinia 2\nlinia 3\n")

    for linie in citeste_linii("test.txt"):
        print(">", linie)