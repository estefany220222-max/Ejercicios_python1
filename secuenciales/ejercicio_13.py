
#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada 
#y su raíz cúbica. PSeInt no tiene ninguna función predefinida que
# permita calcular la raíz cúbica, ¿Cómo se puede calcular?

import math
num1 = int(input("Introduce un numero: "))

raiz_cuabrada = math.sqrt(num1)

raiz_cubica = num1 ** (1/3)

print("la raiz cuabrada de tu numero es: ",raiz_cuabrada)
print("la raiz cubica de tu numero es: ",raiz_cubica)



