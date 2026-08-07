def numara_apeluri(f):
    def wrapper(*args, **kwargs):
        wrapper.apeluri = wrapper.apeluri + 1
        print("[apel #" + str(wrapper.apeluri) + "]", f.__name__)
        return f(*args, **kwargs)
    wrapper.apeluri = 0
    return wrapper

def filtreaza(l, conditie):
    for x in l:
        if conditie(x):
            yield x

def perechi(l):
    for i in range(len(l)):
        yield (i, l[i])

@numara_apeluri
def suma_patrate(n):
    return sum(x * x for x in range(n))

if __name__ == "__main__":
    l = [4, 9, 15, 22, 33, 40, 51]

    print("Pare:", list(filtreaza(l, lambda x: x % 2 == 0)))
    print("Div 3:", list(filtreaza(l, lambda x: x % 3 == 0)))

    for i, val in perechi(l):
        print(i, "->", val)

    print(suma_patrate(10))
    print(suma_patrate(100))
    print("Total apeluri:", suma_patrate.apeluri)