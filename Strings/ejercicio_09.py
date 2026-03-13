frase = input('Ingresa una frase:\n')
word = input('Ingresa una palabra:\n')

if word in frase:
    print(frase.replace(word, f'"{ word }"'))
else:
    print('La palabra NO se encuentra en la frase!')