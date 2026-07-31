import random

N = 1000

frec = {}
for s in range(2, 13):
    frec[s] = 0

for i in range(N):
    z1 = random.randint(1, 6)
    z2 = random.randint(1, 6)
    s = z1 + z2
    frec[s] = frec[s] + 1

print(f"Rezultate dupa {N} aruncari:\n")

for s in range(2, 13):
    proc = frec[s] / N * 100
    bare = round(proc)  
    print(f"{s:2}: {frec[s]:4} ({proc:5.2f}%) {'*' * bare}")

print("\nCea mai frecventa suma ar trebui sa fie 7 - are cele mai multe combinatii.")

ext = random.sample(range(1, 50), 6)
ext.sort()
print("\nExtragere loto:", ext)