year = int(input('Introduce el año: '))

if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
	print(' ')
	print('Año bisiesto')
else:
	print(' ')
	print('Año no bisiesto')