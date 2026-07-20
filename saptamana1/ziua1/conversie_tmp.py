print("-Conversie Temperatura-")
print("1.Celsius -> Fahrenheit")
print("2.Fahrenheit -> Celsius")

op = input("Alege conersia: ")
if op == "1":
    c = float(input("*C: "))
    f = c * 9 / 5 + 32
    print(f"{c} *C = {f:.1f} *F")
elif op == "2":
    f = float(input("*F: "))
    c = (f - 32) * 5 / 9
    print(f"{f} *F = {c:.1f} *C")
else:
    print("Optiune invalida!")