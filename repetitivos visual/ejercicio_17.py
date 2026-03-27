h_a = 0
trabs = int(input("¿Cuántos trabajadores hay en la empresa?: "))
s_h = float(input("Sueldo por hora: "))
for trab in range(1, trabs + 1):
    h_t = 0
    ds = int(input(f"Cuantos días trabajó el trabajador {trab}?: "))
    for d in range(1, ds + 1):
        h= int(input(f"Trabajador {trab}, horas del día {d}: "))
        h_t += h
    print(f"Trabajador {trab} igual sueldo: {h_t * s_h}")
    h_a += h_t

print(f"Pago total a {trabs} trabajadores: {h_a * s_h}")
