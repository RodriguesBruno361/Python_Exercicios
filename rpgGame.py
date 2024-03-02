import random
print('******************')
print('Bem vindo ao simulador de RPG')
print('******************')

enemies = ['Esqueleto', 'Assasino', 'Vampiro', 'Urso']

hp_jogador = 100
num_pocoes = 4
hp_pocao = 30
drop_rate_inimigo = 50
cont_inimigo_morte = 0
player_input1 = ''

while True:
    enemy = random.choice(enemies)
    enemy_health = random.randint(10, 76)
    print('******************')
    print(f'# {enemy} acabou de aparecer #')
    print(f'#Seus Pontos de vida: {hp_jogador}')
    print(f'{enemy} hp: {enemy_health}')
    print('******************')

    while enemy_health > 1:
        print('******************')
        print('O que você irá fazer?')
        print('1.Atacar')
        print('2.Beber uma poção')
        print('3.Correr')
        player_input1 = input('Faça a sua jogada: ')
        if player_input1 == '1':
            enemy_damage = random.randint(10, 40)
            player_damage = random.randint(0, 10)

            enemy_health -= enemy_damage
            hp_jogador -= player_damage

            print(f'Você causou no {enemy} {enemy_damage} pontos de dano neste ataque')
            print(f'Você sofreu {player_damage} de dano')
            print(f'Seu hp: {hp_jogador}')
            print(f'{enemy}´s hp: {enemy_health}')
            if hp_jogador < 1:
                print('Você está muito fraco para batalhar agora!\n Você está prestes a morrer.')
                break
        elif player_input1 == '2':
            if num_pocoes > 0:
                print('Você bebeu uma poção!')
                hp_jogador += hp_pocao
                num_pocoes -= 1
                print(f'Seu HP: {hp_jogador}')
                print(f'Agora você tem {num_pocoes}')
            else:
                print('Você não tem nem uma poção!')
                print('Você precisa matar um inimigo para ganhar uma poção.')
        elif player_input1 == '3':
            print(f'Você fugiu do {enemy}')
            break
        else:
            print('Comando invalido! Digite 1, 2 ou 3.')
        if hp_jogador < 0:
            print('Obrigado por jogar rpgGame!')
            print('******************')
            cont_inimigo_morte += 1
            if random.randint(0, 100) > drop_rate_inimigo:
                print(f'{enemy} deixou cair uma poção.')
                num_pocoes += 1
                print(f'Agora você tem {num_pocoes}')
                print('******************')
        if cont_inimigo_morte == 3:
            while True:
                print('O que você deseja fazer?')
                print('1.Continue Lutando')
                print('2.Sair')
                player_input1 = input('Faça a sua jogada: ')
                if player_input1 == '1':
                    print('Continuar explorando a caverna...')
                    cont_inimigo_morte = 0
                    break
                elif player_input1 == '2':
                    print('Você finalmente achou um lugar seguro!')
                    break
                else:
                    print('Comando invalido!')
            if player_input1 == '2':
                print('Obrigado por jogar rpgGame!')
                break