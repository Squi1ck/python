from random import randint
import os

pontuacoes = [100, 80, 60, 40, 30, 20, 10]
pontuacao = 0
numeroSecreto = 0
numInserido = 0
numTentativas = 0
pontuacao = 0
querJogar = "S"

os.system("clear")

while querJogar == "S":
    for _ in range(7):

        numTentativas += 1

        if numeroSecreto == 0:
                for _ in range(1):
                    n = randint(1,100)
                    numeroSecreto = (n)
        
        numInserido = int(input("Insira um número: "))

        while numInserido < 1 or numInserido > 100:
             print("Valor inválido! O valor deve estar entre 1 e 100.")
             numInserido = int(input("Insira um número novamente: "))

        if numInserido > numeroSecreto:
            print(f"O numero Secreto é menor que {numInserido}")

        if numInserido == numeroSecreto:
            pontuacao = pontuacoes[numTentativas - 1]
            print(f"Acertaste o número secreto em {numTentativas} tentativas e tiveste {pontuacao} pontos! ")
            break

        if numInserido < numeroSecreto:
            print(f"O numero Secreto é maior que {numInserido}")

        if numTentativas >= 7:
            print(f"Perdeste! O numero era {numeroSecreto}")
        
    numTentativas = 0
    numeroSecreto = 0
    querJogar = (input("Deseja continuar a jogar(S/N): ")).upper()