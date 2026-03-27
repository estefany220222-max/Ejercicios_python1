def bisiesto(ye):
    if (ye % 4 == 0 and not (ye % 100 == 0)) or ye % 400 == 0:
        bis = True
    else:
        bis = False
    return bis
def d_mes(mes, ye):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        di = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        di = 30
    elif mes == 2:
        if bisiesto(year):
            di = 29
        else:
            di = 28
    return di
def c_juliano(d, mes, ye):
    diaj = 0
    for m in range(1, mes):
        dia_j = dia_j + d_mes(m, ye)
    dia_j = dia_j + d
    return dia_j
def leer_fecha():
    d = int(input("Día: "))
    mes = int(input("Mes: "))
    ye = int(input("Año: "))
    return d, mes, ye
resul = l_f()
d = resul[0]
m = resul[1]
a = resul[2]

print("Día Juliano:", c_juliano(d, m, a))
