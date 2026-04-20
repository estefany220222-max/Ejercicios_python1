#Programa para jugar el juego del ahorcado
import random

#Definir función que obtiene palabra
def get_word():
    # Convertimos la entrada a int() para que los if funcionen
    tema = int(input("Pon el número sobre que tema quieres jugar el ahorcado:\n\t1 ---- COMIDAS\n\t2 ---- ANIMALES\n\t3 ---- DEPORTES\n\t4 ---- ELECTRODOMESTICOS\n\t5 ---- MATERIAS\n\t6 ---- ROPA\nTEMA NÚMERO:  "))
    
    if tema > 6:
        print("Opción no válida")
        tema = int(input("Pon el número sobre que tema quieres jugar el ahorcado:\n\t1 ---- COMIDAS\n\t2 ---- ANIMALES\n\t3 ---- DEPORTES\n\t4 ---- ELECTRODOMESTICOS\n\t5 ---- MATERIAS\n\t6 ---- ROPA\nTEMA NÚMERO:  "))
    if tema == 1:
        # abrir archivo comidas, se almacena en doc
        doc = './comidas.txt' 
    elif tema == 2:
        doc = './animales.txt'
    elif tema == 3:
        doc = './deportes.txt'
    elif tema == 4:
        doc = './electrodomesticos.txt'
    elif tema == 5:
        doc = './materias.txt'
    elif tema == 6:
        doc = './ropa.txt'
        

    with open(doc, 'r') as f:
        # Quitamos espacios en blanco y saltos de línea vacíos
        words = [line.strip() for line in f.readlines() if line.strip()]
    return random.choice(words)


#Definir función que pinte el ahorcado
def draw(errors):
    match(errors):
        case 0:
            ahorcado = '''|------------\n|\n|\n|\n|\n|\n|\n|____________'''
        case 1:
            ahorcado = '''
|------------
|      |
|      
|     
|      
|
|     
|____________
                        '''
        case 2:
            ahorcado = '''
|------------
|      |
|      O
|     
|      
|
|     
|____________
                '''
        case 3:
            ahorcado = '''
|------------
|      |
|      O
|     /|\\
|      
|
|     
|____________
                '''
        case 4:
            ahorcado = '''
|------------
|      |
|      O
|     /|\\
|      0
|     
|
|____________
                '''
        case 5:
            ahorcado = """
|------------
|      |
|      O
|     /|\\
|      0
|     / \\
|
|____________
                """
        case _:
            pass
    print(ahorcado)


#Escriba palabra con guiones y letras
def write_word(word, chars=""):
    dashed_word = ""
    for char in word:
        if char in chars:
            dashed_word += char + " "
        else:
            dashed_word += "_ "
    return dashed_word.strip()


#Definir función juego
def game():
    #Elige palabra
    word = get_word()

    print('\nJuego del ahorcado!!!')
    print('La palabra oculta tiene', len(word), 'letras.')
    
    errors = 0
    chars = ''

    while errors < 5:
        print("\n" + write_word(word, chars))
        char = input("Escribe una letra: ").lower()

        if char in chars:
            print("Ya habías intentado esa letra.")
            continue

        if char in word:
            chars += char
            if write_word(word, chars).replace(" ", "") == word:
                print(f"\t¡Ganaste!\nLa palabra era: {word}")
                break
        else:
            draw(errors)
            errors += 1
            if errors == 5:
                draw(5)
                print(f'\tBuuuu... \n       Perdiste! \nLa palabra era: {word}')

#Inicio del programa
if __name__ == '__main__':
    game()