h_a = 0
s_h = float(input("Introduce el sueldo por hora: "))
for d in range(1, 7):
    hr = int(input(f"Cuántas horas has trabajado el día {d}?: "))
    h_a += hr
print("Horas acumuladas en la semana:", h_a)
print("Sueldo:", s_h * h_a)
