
t = input("Text: ").lower()

f = {}

for c in t:
    if c != " ":
        if c in f:
            f[c] = f[c] + 1
        else:
            f[c] = 1

for c in f:
    print(c, ":", f[c])