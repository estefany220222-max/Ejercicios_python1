#Calcular el perimetro y el area de un rectangulo dada su base y altura

#Para realizar operaciones matemàticas debemos convertir a nùmero

print()

print("Area y perimetro de un rectangulo")

base = input("ingresa la base:")
base = int(base)

altura = int(input("Ingresa la altura: "))

area = base * altura
perimetro = base * 2 + altura *2

print("Area", area)
print("Perimetro", perimetro)