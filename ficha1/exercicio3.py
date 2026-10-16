from random import randint
import os

resposta = "S"

while resposta == "S":
    pontos = [100, 80, 60, 40, 30, 20, 10]
    numSecreto = randint(1,100)
    pontosJogador = 0
    tentativas = 0
    acertou = False
    while tentativas < 7:
        respostaJogador = int(input(f"\n[Tentativa {tentativas + 1}/7] Adivinhe o número entre 1 e 100: "))

        while respostaJogador < 1 or respostaJogador > 100:
            print("O número inserido é inválido! O valor deve estar entre 1 e 100!!")
            respostaJogador = int(input("Tente Novamente: "))

        os.system("clear")

        if respostaJogador == numSecreto:
            print(f"Parabéns!! Acertaste o número secreto em {tentativas} tentativas.")
            pontosJogador = pontos[tentativas - 1]
            print(f"Tens {pontosJogador} pontos.")
            acertou = True
            break


        if respostaJogador > numSecreto:
            print("O número Secreto é menor que a tua tentativa!")
        else:
            print("O número Secreto é maior que a tua tentativa!")

        tentativas = tentativas + 1

    if not acertou:
        print(f"Que pena!!! O número secreto era {numSecreto}")

        resposta = (input("Deseja jogar novamente? (S/N)")).upper()
            








