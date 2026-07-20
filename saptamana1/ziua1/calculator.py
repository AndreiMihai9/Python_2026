print("=== Calculator simplu ===")

a = float(input("Primul număr: "))
b = float(input("Al doilea număr: "))
op = input("Operația (+ - * /): ")

if op == "+":
    r = a + b
elif op == "-":
    r = a - b
elif op == "*":
    r = a * b
elif op == "/":
    if b == 0:
        print("Eroare!")
        r = None
    else:
        r = a / b
else:
    print("Operație invalidă")
    r = None
    
if r is not None:
    print(f"{a} {op} {b} = {r:.2f}")