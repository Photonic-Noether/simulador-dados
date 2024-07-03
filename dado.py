import random

INTERFAZ = """

#####################################
### SCRIPT DE SIMULACION DE DADOS ###
#####################################

Este script simula la tirada de un dado

"""

print(INTERFAZ)

class Dado:
    def __init__(self, numero_caras: int):
        self.numero_caras = numero_caras
        
    def tirada(self) -> int:
        return random.randint(1, self.numero_caras)

numero_caras = int(input("De cuantas caras quieres el dado: "))
dado = Dado(numero_caras)
tirada = dado.tirada()

print(f"El resultado de tu tirada es {tirada}")
