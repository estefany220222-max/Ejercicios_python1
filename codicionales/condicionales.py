#Estructura de control
#if else elseif

'''
if exp_booleana:
	instrucciones

if exp_booleana:
	instrucciones
else:
	instrucciones

if exp_bool:
	instrucciones
elif exp_bool:
	instrucciones
else:
	instrucciones
'''

numero = int(input('Escribe un numero: '))

if numero > 0:
	print("Es un numero positivo")
elif numero == 0:
	print('El numero es 0')
else:
	print('Es un numero negativo')