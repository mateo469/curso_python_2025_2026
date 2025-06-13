
def new_game():
    respuestas = []
    respuestas_correctas = 0
    pregunta_num = 0
    
    for key in preguntas:
        print('-----------------------------')
        print(key)
        
        for i in opciones[pregunta_num]:
            print(i)
            
        respuesta = input('Ingrese (A, B, C, D): ').upper()
        respuestas.append(respuesta)
            
        respuestas_correctas += check_answer(preguntas.get(key), respuesta)
        pregunta_num +=1
            
    display_score(respuestas_correctas, respuestas)
 #---------------------------------------------------------------------   
def check_answer(respuestas_correctas, respuesta):
    if respuestas_correctas == respuesta:
        print('Correcto!')
        return 1
    else:
        print('Incorrecta!')
        return 0

#-----------------------------------------------------------------------
def display_score(respuestas_correctas, respuestas):
    print('----------------------------')
    print('Resultado!')
    print('---------------------------------------------')
    
    print('Respuesta correctas: ', end=" ")
    for i in preguntas:
        print(preguntas.get(i), end=" ")
    print()
    
    print('Tu Respuestas: ', end=" ")
    for i in preguntas:
        print(i, end=" ")
    print()
    
    #Optener el puntaje en porcentaje de las respuestas correctas
    puntaje = int((respuestas_correctas/len(preguntas))*100)
    print('Puntaje ' + str(puntaje) + '%')

#-------------------------------------------------------------------------------------------
def play_again():
    respuesta = input('QUIERES JUGAR DE NUEVO, SI, NO: ').upper()
    if respuesta == 'SI':
        return True
    else:
        return False

#------------------------------------------------------------------------------------------------
preguntas = {
    'Que idioma se habla en Brasil?': 'A',
    'Cual es el oceano mas grande del mundo?': 'B',
    'Cual es la estrella mas cerca de la tierra?': 'C',
    'Cual es el segundo pais mas grande del mundo?': 'A'
}

#   Crear un arreglo para las opciones de respuestas
opciones = [['A. Portugues', 'B. Español', 'C. Brasileño', 'D. Ingles'],
            ['A. Atlantico', 'B. Pacifico', 'C. Artico', 'D. Indico'],
            ['A. La Luna', 'B. Alfa Centauri A', 'C. El sol', 'D. Ninguna'],
            ['A. Canada', 'B. Rusia', 'C. EE.UU', 'D. Ninguna']]


new_game()
while play_again():
    new_game()
print('Cerrado')