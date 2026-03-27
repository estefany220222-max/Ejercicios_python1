car = input('Escribe una letra(" " para salir)')
while True:
	car = input('Escribe una letra (" " para salir): ')

	if car == ' ':
		break
	if len(car) == 1:
		if car.upper() == 'A' \
			or car.upper() == 'E' \
			or car.upper() == 'I' \
			or car.upper() == 'O' \
			or car.upper() == 'U' \
			print('Vocal')
		else:
			print("no vocal")

	if car == ' ':
		break

	
