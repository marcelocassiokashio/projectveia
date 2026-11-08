def criar_tabuleiro():
    tabuleiro = []

    for i in range(3):
        tabuleiro.append([" "," "," "])

    return tabuleiro 

def mostrar_tabuleiro(tabuleiro):
    print("1   2   3")

    for linha in range(3):
        print(linha + 1, end="  ")

        for coluna in range(3):
            print(tabuleiro[linha][coluna], end="")

            if coluna < 2:
                print(" | ", end="")

        print()

        if linha < 2:
            print("  -----------")
            
def ler_posicao(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor.isdigit():
            numero = int(valor)

            if numero >= 1 and numero <= 3:
                return numero - 1

        print("Digite um número entre 1 e 3!")

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if (tabuleiro[i][0] == jogador and
            tabuleiro[i][1] == jogador and
            tabuleiro[i][2] == jogador):
            return True

        if (tabuleiro[0][i] == jogador and
            tabuleiro[1][i] == jogador and
            tabuleiro[2][i] == jogador):
            return True

    if (tabuleiro[0][0] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][2] == jogador):
        return True

    if (tabuleiro[0][2] == jogador and
        tabuleiro[1][1] == jogador and
        tabuleiro[2][0] == jogador):
        return True

    return False

def verificar_empate(tabuleiro):
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == " ":
                return False

    return True

def jogar():
    tabuleiro = criar_tabuleiro()
    jogadores = ("X", "O")
    casas_usadas = set()
    vez = 0

    while True:
        mostrar_tabuleiro(tabuleiro)

        jogador = jogadores[vez]

        print("Vez do jogador:", jogador)

        linha = ler_posicao("Escolha a linha (1-3): ")
        coluna = ler_posicao("Escolha a coluna (1-3): ")

        posicao = (linha, coluna)

        if posicao in casas_usadas:
            print("Essa casa já está ocupada!")
            continue

        casas_usadas.add(posicao)
        tabuleiro[linha][coluna] = jogador

        if verificar_vitoria(tabuleiro, jogador):
            mostrar_tabuleiro(tabuleiro)
            print("Jogador", jogador, "venceu!")
            return jogador

        if verificar_empate(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("A partida terminou em empate!")
            return "E"

        vez = 1 - vez

def mostrar_regras():
    print("=== REGRAS DO JOGO ===")
    print("Dois jogadores participam.")
    print("O jogador X começa.")
    print("Cada jogador escolhe uma linha e uma coluna.")
    print("Vence quem formar uma linha de três símbolos iguais.")
    print("Se o tabuleiro ficar cheio, ocorre empate.")


def mostrar_placar(placar):
    print("=== PLACAR ===")
    print("Jogador X:", placar["X"], "vitórias")
    print("Jogador O:", placar["O"], "vitórias")
    print("Empates:", placar["E"])

    
def mostrar_historico(historico):
    print("=== HISTÓRICO ===")

    if len(historico) == 0:
        print("Nenhuma partida foi realizada.")
    else:
        for i in range(len(historico)):
            print("Partida", i + 1, ":", historico[i])

def menu():
    placar = {"X": 0, "O": 0, "E": 0}
    historico = []

    while True:
        print("===== JOGO DA VELHA =====")
        print("1 - Jogar")
        print("2 - Regras")
        print("3 - Placar")
        print("4 - Histórico")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            resultado = jogar()
            placar[resultado] += 1
            historico.append(resultado)

        elif opcao == "2":
            mostrar_regras()

        elif opcao == "3":
            mostrar_placar(placar)

        elif opcao == "4":
            mostrar_historico(historico)

        elif opcao == "5":
            print("Obrigado por jogar!")
            break

        else:
            print("Opção inválida!")
            
menu()