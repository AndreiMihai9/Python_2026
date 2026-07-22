import random

print("=====Creeaza-ti propria parola sigura!=====")
x = int(input("Cat de lunga sa fie parola?: "))
l = int(input("Cate litere/caractere sa contina parola?: "))

litere = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%"
cifre = "0123456789"

if l > x:
    print("Nu poti alege mai multe litere decat totalul de caractere a parolei!")
else:
    c = x - l 

    char = []

    for i in range(l):
        char.append(random.choice(litere))

    for i in range(c):
        char.append(random.choice(cifre))

    random.shuffle(char)
    p = "".join(char)

    print(p)
