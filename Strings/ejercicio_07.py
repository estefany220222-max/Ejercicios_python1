cadena = input('Dame una frase: ')

while True:
    letra_1 = input('Ingresa una letra: ')
    if len(letra_1) == 1:
        break

while True:
    letra_2 = input('Ingresa una letra para sustituir la primera: ')
    if len(letra_2) == 1:
        break

frase_nueva = ''
for letra in cadena:
    if letra == letra_1:
        frase_nueva = frase_nueva + letra_2
    else:
        frase_nueva += letra

print()
print('La frase nueva queda asi:\n' + frase_nueva)

frase_2 = cadena.replace(letra_1, letra_2)
print('La frase nueva queda asi:\n' + frase_2)