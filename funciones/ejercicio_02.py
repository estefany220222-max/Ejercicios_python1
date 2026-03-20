def es_Multiplo(num1, num2):
    return num1 % num2 == 0

#def es_multiplo (num1, num2):
    # residuo = num1 % num2
    # if residuo == 0:
    #     return True
    # else:
    #     return False

if __name__ == '__main__':
    num1 = int(input('Ingresa un numero: '))
    num2 = int(input('Ingresa otro numero: '))
    if es_Multiplo(num1, num2):
        print(f"{ num1 } es multiplo de { num2 }")
    else:
        print(f"{ num1 } no es multiplo de { num2 }")