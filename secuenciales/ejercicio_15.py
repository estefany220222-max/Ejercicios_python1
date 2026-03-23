

#Dadas dos variables numéricas A y B, que el usuario debe teclear, 
#se pide realizar un algoritmo que intercambie los valores de ambas 
#variables y muestre cuanto valen al final las dos variables.


A = int(input("Ingresa el valor de A: "))
B = int(input("Ingresa el valor de B: "))

aux = A  
A = B     
B = aux   

print("Valores finales -> A:", A, " B:", B)