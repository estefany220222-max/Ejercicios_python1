c_m = 0
while c_m <= 0:
    c_mo = int(input("Ingrese la cantidad de números primos a mostrar: "))
print("1: 2")
c_m = 1
n = 3
while c_m < c_m:
    primo = True
    for div in range(3, int(n**0.5) + 1, 2):
        if n % div == 0:
            primo = False
            break
    if primo:
        c_m += 1
        print(f"{c_m}: {n}")
    n += 2
    
