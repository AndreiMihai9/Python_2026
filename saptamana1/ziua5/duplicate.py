
l = [3, 1, 4, 1, 5, 3, 9, 4, 3]

print("Lista originala: ", l)

fd = list(set(l))
print("A (set):  ", fd)

fd = []
for x in l:
    if x not in fd:
        fd.append(x)
print("B (manual): ", fd)

fd = []
v = set()
for x in l:
    if x not in v:
        fd.append(x)
        v.add(x)
print("C (set+lista):  ", fd)