x = int(input("Introdu un numar pentru a vedea tabla inmultirii acestuia: "))
n = int(input("Numarul de multiplicari dorite: "))

for i in range(1, n + 1):
    print(f"{x} x {i} = {x * i}")
