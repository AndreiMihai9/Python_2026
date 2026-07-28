
cuv = ["mar", "portocala", "pai", "banana", "kiwi", "capsuna"]

#filter
cuvl_filter = list(filter(lambda c: len(c) > 4, cuv))

#comprehension
cuvl_comp = [c for c in cuv if len(c) > 4]

print("Toate:         ", cuv)
print("Lungi (filter):", cuvl_filter)
print("Lungi (comp):  ", cuvl_comp)

# numere divizibile cu 3
nr = [1, 3, 6, 7, 9, 10, 12, 15]
nrd3 = [n for n in nr if n % 3 == 0]
print("Div. cu 3:     ", nrd3)