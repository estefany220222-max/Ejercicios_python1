h_a = 0
trab = int(input("¿Cuántos trabajadores tiene la empresa?: "))
s_h = float(input("Sueldo por hora: "))

for trab in range(1, trab + 1):
    h_s = int(input(f"Cuántas horas ha trabajado el trabajador {trab}: "))
    h_a += h_s
    print(f"El trabajador {trab} tiene de sueldo {h_s * s_h}")

print(f"El pago de los {trab} trabajadores es: {h_a * s_h}")
