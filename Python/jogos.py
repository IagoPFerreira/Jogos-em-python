import forca
import advinhacao

def escolhe_jogo():
    print("*" * 20)
    print('Escolha o seu jogo ')
    print("*" * 20)

    print('(1) Forca (2) Adivinhação')

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando adivinhação")
        advinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()