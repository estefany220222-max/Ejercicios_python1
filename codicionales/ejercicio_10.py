x1 = float(input("Dime coordenada x de la primera frecuencia: "))
y1 = float(input("Dime coordenada y de la primera frecuencia: "))
r1 = float(input("Dime radio de la primera circunferencia: "))
x2 = float(input("Dime coordenada x de la segunda frecuencia: "))
y2 = float(input("Dime coordenada y de la segunda frecuencia: "))
r2 = float(input("Dime radio de la segunda circunferencia: "))

distancia = ((x2 -x1)**2 + (y2 - y1)**2)**0.5

if distancia > r1+r2:
	print(' ')
	print('circunferencias eexteriores')
if distancia == r1+r2:
	print(' ')
	print('circunferencias tangentes exteriores')
if distancia < r1+r2 and distancia > r1-r2:
	print(' ')
	print('Circunferencias secantes')
if distancia == r1-r2:
	print(' ')
	print('circunferencias tangentes interiores')
if distancia == 0 and distancia < r1-r2:
	print(' ')
	print('circunferencias interiores')
if distancia == 0:
	print(' ')
	print('circunferencias concèntricas')