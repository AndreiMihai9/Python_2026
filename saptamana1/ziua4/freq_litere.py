x = str(input("Scrie o propozitie:"))
s = ""
f = [0] * 26

for i in x:
    if "a" <= i <= "z":
        p = ord(i) - ord("a")
        f[p] += 1

for i in range(0, 26):
 if f[i] > 0:
    l = chr(i + ord("a"))
    print(f"{l} apare de {f[i]} ori!")

"""
x = x.replace(" ","")
x = x.lower()
for i in x:
    if  i not in s:
        print(f"{i} apare de {x.count(i)} ori!")
        s = s + i 

"""