def calcular_factorial(num):
    if num == 1:
        fact = 1
    else:
        fact = num * cfact(num - 1)
    return fact
num1 = int(input("Número: "))
print("El factorial es:", cfact(num1))
