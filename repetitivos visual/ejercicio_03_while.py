suma = 0
cont = 0
print("Número (0 para salir): ")
num = int(input())
while num != 0:
    suma = suma + num
    cont = cont + 1
    print(("Número (0 para salir): "))
    num = int(input())
if cont > 0:
    media = suma // cont
else:
    media = 0

print("Suma:", suma)
print("Media:", media)