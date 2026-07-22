x = int(input("Cate elemente din sirul lui Fibonacci vrei sa scrii: "))
a = 0
b = 1
for i in range(x+1):
   print(f" {a}")
   v = a + b
   a = b 
   b = v
