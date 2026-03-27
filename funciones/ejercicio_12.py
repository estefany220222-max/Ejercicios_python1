def bisiesto(year):
    if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
        bis = True
    else:
        bis = False
    return bisiesto
def d_mes(mes, year):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias = 30
    elif mes == 2:
        if bisiesto(year):
            dias = 29
        else:
            dias = 28
    else:
        dias = 0
    return dias
def v_f(day, mes, year):
    if day < 1 or day > d_mes(month, year):
        esvalida = False
    else:
        esvalida = True
    return esvalida
def c_juliano(day, mes1, year):
    diaj = 0
    for mes1 in range(1, mes):
        diaj = diaj + d_mes(mes1, year)
    diaj = diaj + day
    return diaj
def l_f():
    fvalida = False
    while fvalida == False:
        day2 = int(input("Día: "))
        mes = int(input("Mes: "))
        year = int(input("Año: "))
        fvalida = v_f(day2, mes, year)
        if fvalida == False:
            print("Fecha no válida")
    return day2, mes, year
resultado = l_f()
d = resul[0]
m = resul[1]
a = resul[2]
print("Día Juliano:", c_juliano(d, m, a))

