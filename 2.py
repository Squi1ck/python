import random

# ---------- FUNÇÕES ----------
def inimigos_vivos(inimigos):
    # list comprehension: só os inimigos com vida > 0
    return [inimigo for inimigo in inimigos if inimigo["vida"] > 0]


def mostrar_menu():
    print()
    print("========== BATALHA ==========")
    print("1 — Atacar inimigo")
    print("2 — Consultar estado do jogador")
    print("3 — Listar inimigos vivos")
    print("4 — Usar poção de cura")
    print("5 — Fugir / terminar jogo")


def atacar(jogador, inimigos):
    # devolve 1 se derrotou o inimigo, 0 caso contrário
    vivos = inimigos_vivos(inimigos)
    if len(vivos) == 0:
        print("Não existem inimigos vivos.")
        return 0

    print("Inimigos vivos:")
    for i in range(len(vivos)):
        print(f"{i + 1} - {vivos[i]['nome']} | Vida: {vivos[i]['vida']} | Ataque: {vivos[i]['ataque']}")

    # números aceites: "1", "2", ... até ao nº de inimigos vivos
    validos = [str(n) for n in range(1, len(vivos) + 1)]
    escolha = input("Escolha o inimigo: ")

    if escolha not in validos:
        print(f"Escolha inválida! Introduza um número entre 1 e {len(vivos)}.")
        return 0

    alvo = vivos[int(escolha) - 1]

    # ataque do jogador
    dano = random.randint(10, 20)
    alvo["vida"] -= dano
    if alvo["vida"] < 0:
        alvo["vida"] = 0
    print(f"Causaste {dano} de dano ao {alvo['nome']}.")

    if alvo["vida"] == 0:
        jogador["pontos"] += alvo["pontos"]
        print(f"{alvo['nome']} foi derrotado! Ganhaste {alvo['pontos']} pontos.")
        return 1

    # contra-ataque
    dano_inimigo = random.randint(5, alvo["ataque"])
    jogador["vida"] -= dano_inimigo
    if jogador["vida"] < 0:
        jogador["vida"] = 0
    print(f"{alvo['nome']} contra-atacou e causou {dano_inimigo} de dano.")
    return 0


def consultar_estado(jogador, inimigos, derrotados):
    print("--- Estado do jogador ---")
    print(f"Vida: {jogador['vida']}")
    print(f"Pontuação: {jogador['pontos']}")
    print(f"Inimigos derrotados: {derrotados}")
    print(f"Inimigos vivos: {len(inimigos_vivos(inimigos))}")
    print(f"Poções disponíveis: {jogador['pocoes']}")


def listar_inimigos(inimigos):
    vivos = inimigos_vivos(inimigos)
    if len(vivos) == 0:
        print("Não existem inimigos vivos.")
    else:
        for inimigo in vivos:
            print(f"{inimigo['nome']} | Vida: {inimigo['vida']} | Ataque: {inimigo['ataque']}")


def usar_pocao(jogador):
    if jogador["pocoes"] == 0:
        print("Não tens poções.")
    elif jogador["vida"] >= 100:
        print("A tua vida já está em 100. Não podes usar poção.")
    else:
        jogador["vida"] += 25
        if jogador["vida"] > 100:
            jogador["vida"] = 100
        jogador["pocoes"] -= 1
        print(f"Usaste uma poção. Vida: {jogador['vida']} | Poções restantes: {jogador['pocoes']}")


# ---------- PROGRAMA PRINCIPAL ----------
print("==============================")
print("        JOGO DE BATALHA")
print("==============================")

# Dicionário do jogador
jogador = {"vida": 300, "ataque": 20, "pocoes": 2, "pontos": 0}

# Lista de dicionários com os tipos de inimigo
tipos = [
    {"nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    {"nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    {"nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
    {"nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
    {"nome": "Dragão", "vida": 100, "ataque": 20, "pontos": 500},
]

# Escolher entre 3 e 5 inimigos (copy() para cada um ter a sua própria vida)
inimigos = []
for i in range(random.randint(3, 5)):
    inimigos.append(random.choice(tipos).copy())

print(f"Apareceram {len(inimigos)} inimigos!")

derrotados = 0
resultado = ""

while resultado == "":
    mostrar_menu()
    opcao = input("Opção: ")

    if opcao == "1":
        derrotados += atacar(jogador, inimigos)
    elif opcao == "2":
        consultar_estado(jogador, inimigos, derrotados)
    elif opcao == "3":
        listar_inimigos(inimigos)
    elif opcao == "4":
        usar_pocao(jogador)
    elif opcao == "5":
        resultado = "FUGA"
    else:
        print("Opção inválida! Escolha de 1 a 5.")

    # Condições de fim de jogo (só se ainda não fugiu)
    if resultado == "":
        if jogador["vida"] <= 0:
            resultado = "DERROTA"
        elif len(inimigos_vivos(inimigos)) == 0:
            resultado = "VITÓRIA"

# ---------- MENSAGEM FINAL ----------
print()
print("==============================")
if resultado == "VITÓRIA":
    print("VITÓRIA! Derrotaste todos os inimigos!")
elif resultado == "DERROTA":
    print("DERROTA! A tua vida chegou a zero.")
else:
    print("Partida terminada por FUGA. A fuga não é uma vitória.")
print(f"Resultado: {resultado}")
print(f"Pontuação final: {jogador['pontos']}")
print(f"Inimigos derrotados: {derrotados}")
print("==============================")
