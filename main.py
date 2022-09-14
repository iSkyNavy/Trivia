import random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print(MAGENTA + "Bienvenido a mi trivia sobre desarrollo de software" + RESET)
print(CYAN + "Pondremos a prueba tus conocimientos" + RESET)
score = random.randint(1, 10)
good = 10
bad = 5
starting_trivia = True
attempts = 0
print(
    CYAN + "Tu puntaje inicial es ", score,
    "\nEl juego comenzara en 5s, veremos con cuanto puntaje terminas.." +
    RESET)

for x in range(0, 5, +1):
    time.sleep(1)
nombre = input("Ingresa tu nombre: ")

print(
    BLUE + "\nHola", nombre,
    "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
    + RESET)
while starting_trivia == True:
    attempts += 1
    print("\nIntento número:", attempts)
    input("Presiona Enter para continuar")
    # Pregunta 1
    print("\n", YELLOW + "1) ¿Qué significa HTML?" + RESET)
    print("a) Hyper text meta language")
    print("b) Hype Talent More Language")
    print("c) HyperText Markup Language")
    print("d) NA")
    respuesta_1 = input("\nTu respuesta: ")
    while respuesta_1 not in ("a", "b", "c", "d", "x"):
        respuesta_1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta_1 == "a":
        print("Incorrecto ", nombre, "la respuesta es c")
        score -= bad
    elif respuesta_1 == "b":
        print("Incorrecto ", nombre, "la respuesta es c")
        score -= bad
    elif respuesta_1 == "d":
        print("Incorrecto ", nombre, "la respuesta es c")
        score -= bad
    elif respuesta_1 == "x":
        print("Rspt secret ", nombre, "la respuesta es genial y secreta")
        score += 1200
    else:
        print("Correcto ", nombre, "la respuesta es c")
        score += good
    time.sleep(2)
    print("Su score hasta ahora es", score, "\n")

    # Pregunta 2
    print(YELLOW + "2) ¿Cuál no es un lenguaje de programación?" + RESET)
    print("a) Javascript")
    print("b) Golang")
    print("c) PHP")
    print("d) HTML")
    respuesta_2 = input("\nTu respuesta: ")
    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta_2 == "a":
        print("Incorrecto ", nombre, "la respuesta es d")
        score -= bad
    elif respuesta_2 == "b":
        print("Incorrecto ", nombre, "la respuesta es d")
        score -= bad
    elif respuesta_2 == "c":
        print("Incorrecto ", nombre, "la respuesta es d")
        score -= bad
    else:
        print("Correcto ", nombre, "la respuesta es d")
        score += good
    time.sleep(2)
    print("Su score hasta ahora es", score, "\n")

    # Pregunta 3
    print(YELLOW + "3) ¿Cuál es una caracteristica del desarrollo frontend?" +
          RESET)
    print("a) Trabaja con bases de datos directamente")
    print("b) El lenguaje se ejecuta en el servidor")
    print("c) Utiliza un framework popular llamado REACT.JS")
    print("d) NA")
    respuesta_3 = input("\nTu respuesta: ")
    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta_3 == "a":
        print("Incorrecto ", nombre, "la respuesta es c")
        score -= bad
    elif respuesta_3 == "b":
        print("Incorrecto ", nombre, "la respuesta es c")
        score -= bad
    elif respuesta_3 == "d":
        print("Incorrecto ", nombre, "la respuesta es c")
        score -= bad
    else:
        print("Correcto ", nombre, "la respuesta es c")
        score += good
    time.sleep(2)
    print("Su score hasta ahora es", score, "\n")
    # Pregunta 4
    print(YELLOW + "4) ¿En que año se creo el lenguaje Python?" + RESET)
    print("a) 1989")
    print("b) 1988")
    print("c) 1600")
    print("d) 2000")
    respuesta_4 = input("\nTu respuesta: ")
    while respuesta_4 not in ("a", "b", "c", "d"):
        respuesta_4 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    if respuesta_4 == "b":
        print("Masomenos ", nombre, "la respuesta es a")
        score += 5
    elif respuesta_4 == "c":
        print("Disparatado ", nombre, "la respuesta es a")
        score = score / 2
    elif respuesta_4 == "d":
        print("Malo ", nombre, "la respuesta es a")
        score -= 5
    else:
        print("Correcto ", nombre, "la respuesta es a")
        score = score * 2
    time.sleep(5)
    for x in range(random.randint(1, 5), random.randint(6, 10), +1):
        score = score + x
    print("Su score final es", score, "\n")
    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )

    score = 0
    if repetir_trivia != "si":
        print(f"\nEspero {nombre} que lo hayas pasado bien, hasta pronto!")
        starting_trivia = False
