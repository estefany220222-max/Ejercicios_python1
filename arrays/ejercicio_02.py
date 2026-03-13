
vector = []

vector_reverse = []

for i in range(1, 6):
    letra = input(f'Inserta cadena de texto {i}: ')
    vector.append(letra)


for i in range(4, -1, -1):
    vector_reverse.append(vector[i])

print(vector)
print(vector_reverse)