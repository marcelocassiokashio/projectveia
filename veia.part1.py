def criar_tabuleiro():
    tabuleiro = []

    for i in range(3):
        tabuleiro.append([" "," "," "])

    return tabuleiro 

def mostrar_tabuleiro(tabuleiro):
    print("\n   1   2   3")

    for linha in range(3):
        print(linha + 1, end="  ")

        for coluna in range(3):
            print(tabuleiro[linha][coluna], end="")

            if coluna < 2:
                print(" | ", end="")

