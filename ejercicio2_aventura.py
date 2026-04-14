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
def mostrar_fecha():
    ahora = datetime.now()
    print(f"Fecha: {ahora.day}/{ahora.month}/{ahora.year}")
print("=== GENERADOR DE AVENTURAS ===")
mostrar_fecha()
print("=== Heroes Generados ===")
for i in range(1, 4):
    nombre = generar_nombre()
    clase = generar_clase()
    hp = generar_hp()
    print(f"Heroe {i}: {nombre} | Clase: {clase} | HP: {hp}")
