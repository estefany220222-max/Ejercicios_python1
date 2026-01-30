'''Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.'''
minutos = int(input('Ingrese los minutos: '))
horas = minutos // 60
min_res = minutos % 60
print(" ")
print('minutos que ingreso:', minutos)
print('horas:', horas)
print('minutos:', min_res)