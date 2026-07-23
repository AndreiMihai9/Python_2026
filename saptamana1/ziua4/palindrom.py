x = str(input("Introdu un cuvant sau o propozitie: "))

x = x.lower()
x = x.replace(" ","")

if x == x[:: -1]:
    print("Cuvantul este palindrom!")
else:
    print("Cuvantul nu este palindrom!")