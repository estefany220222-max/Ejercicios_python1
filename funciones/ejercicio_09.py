def intercambiar(may, men):
    if may < men:
        aux = may
        may = men
        men = aux
    return may, men
def cal_mcd(num1, num2):
    resul = intercambiar(num1, num2)
    num1 = resul[0]
    num2 = resul[1]
    resto = num1 % num2
    if resto == 0:
        mcd = num2
    else:
        mcd = cal_mcd(num2, resto)
    return mcd
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
print("MCD:", cal_mcd(n1, n2))
