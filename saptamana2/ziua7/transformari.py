tc = [0, 20, 37, 100, -5]

#map
tf_map = list(map(lambda c: c * 9 / 5 + 32, tc))

#comprehension
tf_comp = [c * 9 / 5 + 32 for c in tc]

print("Celsius: ", tc)
print("F (map): ", tf_map)
print("F (comp):", tf_comp)


nr = [1, 2, 3, 42, 100]
nrs = list(map(str, nr))
print("Stringuri: ", nrs)