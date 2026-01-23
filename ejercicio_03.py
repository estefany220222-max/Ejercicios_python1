#Dados los catetos de un triangulo rectangulo
#Calcular la hipotenusa

#hipotenusa**2 = cat_1**2 + cat_2**2

print()

cateto_1 = int(input('Ingresa el cateto 1: '))
cateto_2 = int(input('Ingresa el cateto 2: '))

print()

hipotenusa = (cateto_1 ** 2 + cateto_2 ** 2) ** (1/2)

print("La hipotenusa es:", hipotenusa)