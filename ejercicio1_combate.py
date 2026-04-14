def calcular_dano:
    dano = ataque - defensa
    if dano < 0:
        return 0
    return dano
def aplicar_dano:
    nuevo_hp = hp_actual - dano
    if nuevo_hp < 0:
        return 0
    return nuevo_hp
def mostrar_estado:
    print(f"{nombre}: {hp}/{hp_max}")
def realizar_ataque:
    print(f"{atacante} ataca a {defensor} por {dano} de dano!")
hp_heroe = 100
hp_enemigo = 50
print("=== Estado Inicial ===")
mostrar_estado("Heroe", hp_heroe)
mostrar_estado("Enemigo", hp_enemigo)
dano_fijo = calcular_dano(25, 10)
realizar_ataque("Heroe", "Enemigo", dano_fijo)
hp_enemigo = aplicar_dano(hp_enemigo, dano_fijo)
mostrar_estado("Enemigo", hp_enemigo)
realizar_ataque("Heroe", "Enemigo", dano_fijo)
hp_enemigo = aplicar_dano(hp_enemigo, dano_fijo)
mostrar_estado("Enemigo", hp_enemigo)
