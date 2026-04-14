import random
from datetime import datetime
def generar_nombre():
    nombres = ["Link", "Zelda", "Mario", "Samus", "Kirby"]
    return random.choice(nombres)
def generar_clase():
    clases = ["Guerrero", "Mago", "Arquero", "Explorador"]
    return random.choice(clases)
def generar_hp():
    return random.randint(80, 120)
  
