import random
def c_max_min(vect, size):
    mx = vect[0]
    mn = vect[0]
    for i in range(size):
        if mx < vect[i]:
            mx = vect[i]
        if mn > vect[i]:
            mn = vect[i]
    return mx, mn
s_list = 10
lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(s_list):
    lista[i] = random.randint(1, 100)
resul = c_max_min(lista, size_lista)
mx = resul[0]
mn = resul[1]
print("El valor máximo es", mx)
print("El valor mínimo es", mn)
