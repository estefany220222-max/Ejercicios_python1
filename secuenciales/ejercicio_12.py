

#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen 
#dos puntos en el plano. Calcula y muestra la distancia entre ellos.

print("Tienes que colocar 2 pares de numeros")
print("para saber la distancia entre ellos")
print("")
x1 = int(input("Coordenada X: "))
y1= int(input("Coordenada Y: "))
print("")
x2 = int(input("Coordenada X: "))
y2 = int(input("Coordenada Y: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print("La distancia de las coordenadas es de: ",distancia)