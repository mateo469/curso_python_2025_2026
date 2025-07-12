#Aprenderemos como encriptar un archivo de la manera mas basica
def encriptar(texto):
    #print('Texto encriptado ' + texto)
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    print('Texto encriptado: ' + textoFinal)
#encriptar('bienvenidos')
def desencriptar(texto):
    textoFinal = ''
    for i in range(0, len(texto), 2):  # Saltamos de 2 en 2
        textoFinal += texto[i]
    print('Texto desencriptado: ' + textoFinal)
    
encriptar('bienvenidos')
desencriptar('bxixexnxvxexnxixdxoxsx')