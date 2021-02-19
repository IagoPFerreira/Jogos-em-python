def jogar():

    import random

    print("*" * 20)
    print('Bem vindo ao jogo de advinhação')
    print("*" * 20)

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_de_tentativas = 20

    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input('Digite um número entre 1 e 100: ')
        print(f'Voce digitou {chute_str}')
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print('Você deve digitar um número entre 1 e 100')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você acertou')
            break
        elif maior:
            print('Você errou! Seu chute foi maior que o número secreto')
        elif menor:
            print('Você errou! Seu chute foi menor que o número secreto')

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print('Fim de jogo')
    print(f'O número era {numero_secreto}')
    print(f'A sua pontuação foi {pontos} pontos')

if __name__ == "__main__":
    jogar()