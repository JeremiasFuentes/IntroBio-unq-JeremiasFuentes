import string
from random import *

palabra_secreta = choice(["Procariota", "Eucariota", "ARN", "SECUENCIA CODIFICANTE", "CELULA", "PROTEINA"])

vidas = 8
print(f"Bienvenido al juego de la vida, he pensado en una palabra secreta, intenta adivinarla tienes {vidas} vidas, en caso de llegar a 0 MORIRAS")

letras_faltantes = list(string.ascii_uppercase)
letras_usadas = []


def actualizar_palabra(palabra, letras):
    nueva_palabra = palabra
    for letra in letras:
        nueva_palabra = nueva_palabra.replace(letra, "_ ")
    return nueva_palabra


def pedir_letra(letras_faltantes):
    letra = ""
    while letra not in letras_faltantes:
        letra = input("Ingresa una letra para ver si esta en la palabra:").upper()
    return letra


juego_terminado = False
while vidas > 0:
    palabra_encriptada = actualizar_palabra(palabra_secreta,letras_faltantes)
    if palabra_encriptada == palabra_secreta:
        print(f"Felicidades!! adivinaste la palabra, era {palabra_secreta}, te salvaste esta vez.")
        break
    print(f"La palabra a adivinar es: {palabra_encriptada} . Te quedan {vidas} vidas")
    letra_input = pedir_letra(letras_faltantes)
    letras_faltantes.remove(letra_input)
    letras_usadas.append(letra_input)
    if palabra_secreta.count(letra_input) > 0:
        print(f"Bien! la letra {letra_input} se encunetra en la palabra")
    else:
        print(f"La letra {letra_input} no se encuentra en la palabra")
        vidas -= 1

if palabra_encriptada != palabra_secreta:
    print(f"Game Over. la palabra era {palabra_secreta}, cuales son tus ultimas palabras?")

