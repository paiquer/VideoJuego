# Aqui importamo el modulo random
import random
import os

# Creamos la funcion principal
def run():

# Lista de las imagenes del juego
    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    # Definimos la base de datos
    DB = [
       "C",
       "PYTHON",
       "JAVASCRIPT",
       "JAVA",
       "PHP"
    ]

    # Hacer palabras aleatoria
    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    # Ciclo infinito
    while True:
        os.system("clear")
        for character in spaces:
            print(character, end=" ")
        print(IMAGES[attemps])
        letter = input("Elige una letra").upper()

        # Creamos una variable que indica si la persona
        # encontro la letra en los ciclos
        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

        # Restar menos 1 a la variable
        if not found:
            attemps -= 1

        # Si no hay guiones bajos el usuario gano
        if "_" not in spaces:
            os.system("clear")
            print("Ganaste")
            break
            input()

        # Si ya no hay intentos perdiste
        if attemps == 0:
            os.system("clear")
            print("Perdiste")
            break
            input()

# Creamos el entrypoint
if __name__ == '__main__':
    run()