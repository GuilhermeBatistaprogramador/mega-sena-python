from random import randint
from time import sleep

# Importando bibliotecas:
# random → para gerar números aleatórios
# time → para criar pausas no programa

palpites = []  # Lista principal que vai armazenar todos os jogos

print('-' * 40)
print(f'{"JOGO DA MEGA SENA":^40}')
print('-' * 40)

# Validação de entrada do usuário
while True:
    try:
        sorteio = int(input('Quantos jogos você quer que eu sorteie? '))
        break
    except ValueError:
        print('Digite apenas números válidos!')

print('-=' * 3, f'SORTEANDO {sorteio} JOGOS', '-=' * 3)
sleep(1)

# Controle da quantidade de jogos
numero = 1
while numero <= sorteio:
    guardar_palpites = []  # Lista temporária para cada jogo

    # Sorteio de 6 números
    for cont in range(0, 6):
        jogador = randint(1, 60)

        # Evita números repetidos no mesmo jogo
        while jogador in guardar_palpites:
            jogador = randint(1, 60)

        guardar_palpites.append(jogador)

    palpites.append(guardar_palpites)  # Adiciona o jogo completo na lista principal
    numero += 1

# Exibição dos jogos
for posicao, jogo in enumerate(palpites):
    print(f'JOGO {posicao + 1}: {jogo}')
    sleep(1)
    
print('=' * 11, 'BOA SORTE', '=' * 11)