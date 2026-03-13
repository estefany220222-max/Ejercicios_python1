#Hacer un programa que inicialice un vector con numeros aleatorios
#y posterior ordene los elementos de menor a mayor

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 1000))

print()
numbers.sort()
print(numbers)
