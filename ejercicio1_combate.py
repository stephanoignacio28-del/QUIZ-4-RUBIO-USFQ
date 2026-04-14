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
