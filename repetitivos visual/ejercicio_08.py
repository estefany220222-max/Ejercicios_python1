sdi = 0
cfi = 0
il = False
while True:
    linf = int(input("Introduce el límite inferior del intervalo: "))
    lsup = int(input("Introduce el límite superior del intervalo: "))
    if linf > lsup:
        print("El límite inferior debe ser menor que el superior.")
    else:
        break
n = int(input("Introduce un número 0 para salir: "))
while n != 0:
    if n > linf and n < lsup:
        sdi += num
    else:
        cfi += 1
    if n == linf or n == lsup:
        il = True
    n = int(input("Introduce un número 0 para salir: "))
print("La suma de los números dentro del intervalo es", sdi)
print("La cantidad de números fuera del intervalo es", cfi)
if il:
    print("Se ha introducido algún número igual a los límites del intervalo.")
else:
    print("No se ha introducido ningún número igual a los límites del intervalo.")
