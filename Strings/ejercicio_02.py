cadena = input('Escribe algo:\n')
subcadena = input('Escribe una subcadena:\n')

if cadena.startswith(subcadena):
    print(cadena, 'Si comienza con', subcadena)
else:
    print(cadena, 'No comienza con', subcadena)