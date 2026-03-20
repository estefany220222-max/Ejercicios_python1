#centrar el texto

def centrar(frase):
    message = ' ' * (40 - len(frase) // 2)
    message += frase
    message += ' ' * (40 - len(frase) // 2)
    print(message)
    print('=' * 80)

message1 = 'Texto a centrar'
centrar(message1)
message2 = 'Otro texto a centrar =D'
centrar(message2)
