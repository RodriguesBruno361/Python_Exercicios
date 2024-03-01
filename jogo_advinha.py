from random import randint

seu_nome = input('Olá, qual o seu nome? ')
print(f'Okay {seu_nome}, eu estou escolhendo um número de 1 até 10. Você consegue advinhar?')

numero_advinhado = randint(1, 10)
numero_tentativas = 3

for tentativa in range(1, numero_tentativas + 1):
    numero_escolhido = int(input('Escolha um número: '))
    if numero_escolhido == numero_advinhado:
        print(f'Parabéns, você acertou em {tentativa} tentativas!')
        break
    elif numero_escolhido > numero_advinhado:
        print('Escolha um número menor')
    else:
        print('Esolha um número maior!')
print(f'O número era {numero_advinhado}. Obrigado por jogar!')