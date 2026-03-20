def temperatura_media(temp1, temp2):
    return (temp1, temp2) / 2

if __name__ == '__main__':
    temps = int(input('Cuantas temperaturas vas a calcular? '))
    for i in temps:
        temp1 = float(input('Ingresa temperatura mínima: '))
        temp2 = float(input('Ingresa temperatura máxima: '))

        print(f'La temperatura media es: { temperatura_media(temp1, temp2) }')