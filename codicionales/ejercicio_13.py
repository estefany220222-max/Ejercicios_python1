

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
year = int(input("Introduce el año: "))

bisiesto = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    max_dias = 31
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    max_dias = 30
elif mes == 2:
    max_dias = 29 if bisiesto else 28
else:
    max_dias = 0  

if mes >= 1 and mes <= 12 and dia >= 1 and dia <= max_dias:
    print("La fecha es correcta.")
else:
    print("La fecha no es correcta.")