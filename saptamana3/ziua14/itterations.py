class NumaraInvers:
    # iterator scris manual: are __iter__ si __next__
    def __init__(self, start):
        self.curent = start

    def __iter__(self):
        return self       

    def __next__(self):
        if self.curent < 0:
            raise StopIteration   
        val = self.curent
        self.curent = self.curent - 1
        return val

if __name__ == "__main__":

    l = ["a", "b", "c"]
    it = iter(l)
    print(next(it))
    print(next(it))
    print(next(it))

    try:
        print(next(it))
    except StopIteration:
        print("Lista s-a terminat.")

    print("\nNumaratoare inversa:")
    for x in NumaraInvers(5):
        print(x, end=" ")
    print()

    nr = NumaraInvers(3)
    print(list(nr))    
    print(list(nr))    