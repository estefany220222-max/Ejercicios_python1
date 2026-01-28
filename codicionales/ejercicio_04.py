''' Programa que hace una division, si el divisor es 0 que termine o que diga que no se puede '''

num_1 = int(input('Ingresa el numero: '))
num_2 = int(input('Ingresa otro numero: '))

if num_2 == 0:
	print('No se puede dividir entre 0')
else:
	divi = num_1 / num_2
	print('La division es:', divi)