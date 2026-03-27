n1 = int(input("Coloca el número 1: "))
n2 = int(input("Coloca el número 2: "))
if n1 % 2 == 1:
    n1 = n1 + 1

for i in range(n1, n2 + 1, 2):
    print(i, "es par")
