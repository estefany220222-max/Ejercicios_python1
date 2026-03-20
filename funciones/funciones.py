'''
funciones de python

print("un texto") -> imprimir en terminal
int('5') -> regresa el valor como entero
input('Texto') -> regresa el texto del teclado
len(objeto) -> regresa el tamaño del objeto
range(5) -> regresa una colección de valores


Podemos crear funciones

--DEFINIR LA FUNCIÓN--
def name_funcion(parametros):
    instrucciones
    return algo

llamar o ejecutar
name_funcion()

'''

#Sin parametros y sin retorno

def hello():
    print('Hello!')

hello()
hello()
hello()

print()

#Con parametros y sin retorno
def hello_2(name):
    print('Hello', name)

hello_2('Spiderman')
hello_2('Cameron')
hello_2('Tachala')
hello_2('My beautiful boyfriend')

print()

#Funciones con parametro y retorno
def duplica(num):
    return num * 2

doble = duplica(15)
print('El doble de 15 es:', doble)

def suma(num1, num2):
    return num1 + num2

result = suma(16, -26)
print()
print(result)

#Parametros posicionales

def fullname(name, ap_pat, ap_mat):
    return f"{ name } { ap_pat } {ap_mat}"

print()
print(fullname("Estefany Areli","Rizo","Fernández"))

#Parametros nombrados
print()
print(fullname(ap_pat = "Rizo",
               ap_mat = "Fernández",
               name = "Estefany Areli"))

#Parametros opcionales
def get_hero(name, hero = 'Superman'):
    return f"{ name } is { hero }"

print()
print(get_hero("Frank"))
print(get_hero("Manuel"))
print(get_hero("Peter Parker", "Spiderman"))