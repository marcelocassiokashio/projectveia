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
