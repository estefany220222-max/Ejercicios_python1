correctas = int(input("Dime cantidad de respuestas correctas: "))
incorrectas = int(input("Dime cantidad de respuestas incorrectas: "))

pnts = correctas * 5 + incorrectas * (-1)

print()
print("Puntos:",pnts)