print("=== Calculator BMI ===")

n = input("Numele tau: ")
g = float(input("Greutatea (kg): "))
i = float(input("Inaltimea (m): "))

bmi = g / (i ** 2)

if bmi < 18.5:
    c = "subponderal"
elif bmi < 25:
    c = "greutate normală"
elif bmi < 30:
    c = "supraponderal"
else:
    c = "obezitate"

print(f"\n{n}, BMI-ul tău este {bmi:.1f}")
print(f"Categorie: {c}")