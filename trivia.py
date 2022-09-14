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
attempts_score_list = []
options_list = []
options_1 = [
    "a) Hyper text meta language", "b) Hype Talent More Language",
    "c) HyperText Markup Language", "d) NA"
]
options_list.append(options_1)
options_2 = ["a) Javascript", "b) Golang", "c) PHP", "d) HTML"]
options_list.append(options_2)
options_3 = [
    "a) Trabaja con bases de datos directamente",
    "b) El lenguaje se ejecuta en el servidor",
    "c) Utiliza un framework popular llamado REACT.JS", "d) NA"
]
options_list.append(options_3)
options_4 = ["a) 1989", "b) 1988", "c) 1600", "d) 2000"]
options_list.append(options_4)


def showOptions(list):
    for e in list:
        print(GREEN + e + RESET)


def showScore(score):
    time.sleep(1)
    print(YELLOW + "Su score hasta ahora es", score, "\n" + RESET)
    time.sleep(2)


def isCorrect(answer, correct_aswer):
    if answer != correct_aswer:
        print(RED + "Incorrecto ", nombre, "la respuesta es ",
              correct_aswer + RESET)
        return -bad
    else:
        print(BLUE + "Correcto ", nombre, "la respuesta es ",
              correct_aswer + RESET)
        return good


def showAttemptsScoreList():
    print("Sus puntajes son: \n")
    for number in range(0, len(attempts_score_list), +1):
        time.sleep(1)
        print("Intento nro: ", number + 1, "=> ", attempts_score_list[number])


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
    input("Presiona Enter para continuar\n")
    # Pregunta 1
    print(YELLOW + "1) ¿Qué significa HTML?" + RESET)
    showOptions(options_list[0])
    respuesta_1 = input("\nTu respuesta: ")
    while respuesta_1 not in ("a", "b", "c", "d", "x"):
        respuesta_1 = input(
            "Debe responder alguna de estas alternativas a,b,c,d, ingresa nuevamente tu respuesta: "
        )
    if respuesta_1 == "x":
        print("Respuesta secret ", nombre, "la respuesta es genial y secreta")
        score += 1200
    else:
        score += isCorrect(respuesta_1, "c")
    showScore(score)

    # Pregunta 2
    print(YELLOW + "2) ¿Cuál no es un lenguaje de programación?" + RESET)
    showOptions(options_list[1])
    respuesta_2 = input("\nTu respuesta: ")
    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    score += isCorrect(respuesta_2, "d")
    showScore(score)

    # Pregunta 3
    print(YELLOW + "3) ¿Cuál es una caracteristica del desarrollo frontend?" +
          RESET)
    showOptions(options_list[2])
    respuesta_3 = input("\nTu respuesta: ")
    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
    score += isCorrect(respuesta_3, "c")
    showScore(score)

    # Pregunta 4
    print(YELLOW + "4) ¿En que año se creo el lenguaje Python?" + RESET)
    showOptions(options_list[3])
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
        print("Correcto ", nombre, "la respuesta es a\n")
        score = score * 2
    time.sleep(5)
    for x in range(random.randint(1, 5), random.randint(6, 10), +1):
        score = score + x
    print("Su score final es", score, "\n")
    attempts_score_list.append(score)
    time.sleep(1)
    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )

    score = 0
    if repetir_trivia != "si":
        showAttemptsScoreList()
        time.sleep(2)
        print(YELLOW + "La suma de tu puntaje es", sum(attempts_score_list),
              RESET)
        time.sleep(1)
        print(
            f"\nEsperamos, {nombre}, que lo hayas pasado bien, hasta pronto!")
        starting_trivia = False
