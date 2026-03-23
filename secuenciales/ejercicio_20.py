euro2 = int(input("Monedas de 2 Euros: "))
euro1 = int(input("Monedas de 1 Euro: "))
cent50 = int(input("Monedas de 50 Céntimos: "))
cent20 = int(input("Monedas de 20 Céntimos: "))
cent10 = int(input("Monedas de 10 Céntimos: "))

teu = (euro2 * 2 + euro1)
cntms = cent50 * 50 + cent20 * 20 + cent10 *10
teu = teu + (cntms / 100)
cntms = cntms % 100

print()
print("Total de euros:", teu, "\nTotal de centimos:", cntms)