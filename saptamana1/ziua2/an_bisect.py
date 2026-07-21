an = int(input("Introdu anul: "))

bisect = (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0)

if bisect:
    print(f"{an} este an bisect.")
else:
    print(f"{an} nu este an bisect.")