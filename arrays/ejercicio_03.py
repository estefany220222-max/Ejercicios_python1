notas = []

for i in range(1, 6):
    nota = int(input(f'Ingresa la nota {i}: '))
    notas.append(nota)
    
suma = 0
minima = 10
maxima = 0

for nota in notas:
    suma += nota
    if nota < minima:
        minima = nota
    if nota > maxima:
        maxima = nota

print()
print('La nota minima es:', minima)
print('La nota maxima es:', maxima)
print('La nota media es:', suma / 5)