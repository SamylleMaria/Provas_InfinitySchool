print('Escolha um número de 1 a 100.')
import random
numero_secreto = random.randint(1,100)
qtd_jogadas = 0
while True:
    escolha = int(input('Digite sua primeira tentativa: '))
    qtd_jogadas +=1
    if escolha > 100 or escolha < 1:
        print('Digite uma entrada válida.')
    elif escolha > numero_secreto:
        print('Você errou. O número secreto é menor que sua escolha. tente novamente.')
    elif escolha < numero_secreto:
        print('Você errou. O número secreto é maior que sua escolha. tente novamente.')
    elif escolha == numero_secreto:
        print(f"Parabéns! Você acertou com {qtd_jogadas}")