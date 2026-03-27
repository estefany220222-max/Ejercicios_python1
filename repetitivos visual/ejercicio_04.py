c_neg = 0
c_pos = 0
c_cero = 0
n1 = int(input("Cuántos numeros vas a introducir?: "))
for i in range(n1):
    print("Número", i + 1, ":")
    n2 = int(input())
    if n2 > 0:
        c_pos += 1
    elif n2 < 0:
        c_neg += 1
    else:
        c_cero += 1

print("Números positivos:", c_pos)
print("Números negativos:", c_neg)
print("Números igual a 0:", c_cero)
