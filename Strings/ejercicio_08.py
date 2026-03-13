frase = input('Ingrese una frase: \n')

frase_nueva = ''
for letra in frase:
    if letra.isupper():
        letra_nueva = letra.lower()
    else:
        letra_nueva = letra.upper()
    frase_nueva += letra_nueva

print()
print(frase)
print(frase_nueva)
