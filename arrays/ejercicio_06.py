#Crear un usuario que pida el numero de mes y regrese cuantos dias tiene y ell nombre del mes

dias = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

mes = int(input('Ingresa un número [1, 12]:\t'))
print('dias:', dias[mes -1])
print('mes:',meses[mes -1])
