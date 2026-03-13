numbers = []

for i in range(10):
    num = int(input('Ingresa un número (0 para salir): '))
    if num == 0:
        break
    else:
        numbers.append(num)

print()
print(numbers)