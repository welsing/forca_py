## O programa inicia com o menu de categorias e uma opção de sair.
## Após o usuario selecionar sua categoria
## O pc vai sortear uma palavra da categoria e iniciar o jogo, a cada loop o usuario vai digitar uma letra ou um comando para sair
## A cada iteração uma função vai verificar: Se a letra está na palavra sorteada e se estiver a letra é revelada na palavra oculta
## Se não estivar na palavra sorteada é verificado se essa letra já foi digitada, caso não, adiciona ele na lista de erros e desconta uma chance do usuario
## Se as chances do usuario acabarem, o loop quebra e o usuario perde.
## Se o usuario acertar todas as letras com um saldo positivo de chances de jogada, então o loop quebra e o usuario ganha um ponto de vitoria e volta para o menu pricipal.

from engine_forca import *
from interacoes import *

wins = 0
while True:
    user = menu(wins) # Mostra o menu
    quit(user)    # Verifica se o usuario quer sair
    if user.strip().lower()[0] in "1234":        # Verifica se é uma opção valida
        user = int(user)
        carregar()
        wins += start_game(user) 
    else:
        print("OPÇÃO \033[1;31mINVALIDA\033[0;0m!")
        carregar()


