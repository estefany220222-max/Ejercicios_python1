num = int(input("Coloca el número para calcular su potencia: "))
pot = int(input("Coloca la potencia para calcular: "))

while pot <= 0:
    print("La potencia debe ser un número positivo. Inténtalo otra vez.")
    pot = int(input("Coloca la potencia para calcular: "))

resul = num ** pot
print(f"La potencia de {num} elevado a {pot} es: {resul}")


    
