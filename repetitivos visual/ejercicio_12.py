a_acum = 0
for m in range(1, 13):
    c_m = float(input(f"¿Cuánto has ahorrado en el mes {m}?: "))
    a_acum += c_m
    print(f"En el mes {m} llevas ahorrado {a_acum}")
