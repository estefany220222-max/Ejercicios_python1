n = int(input("Introduce un número: "))
if n <= 1:
    print(f"{n} no es primo.")
else:
    pri = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            pri = False
            break
    if pri:
        print(f"{n} es primo")
    else:
        print(f"{n} no es primo")
