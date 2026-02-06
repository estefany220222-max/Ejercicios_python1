ladoA = float(input('Introduce longitud del lado A: '))
ladoB = float(input('Introduce longitud del lado B: '))
ladoC = float(input('Introduce longitud del lado C: '))

if ladoA**2 + ladoB**2 == ladoC**2 or ladoB**2+ladoC**2 == ladoA**2 or ladoC**2+ladoA**2 == ladoB**2:
	print('Triangulo rectangulo')
if(ladoA == ladoB and ladoA != ladoC) or (ladoB == ladoC and ladoB != ladoA) or (ladoC == ladoA and ladoC != ladoB):
	print('Triangulo isosceles')
elif ladoA == ladoB and ladoA == ladoC:
	print('Triangulo equilatero')
else:
	print('Triangulo escaleno')