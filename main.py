## O pc vai sortear uma palavra e iniciar o jogo, a cada loop o usuario vai digitar uma letra ou um comando para sair
## A cada iteração uma função vai verificar se o usuario já achou todas as letras 
## e verificar se o usuario tem chances ainda para jogar.
## Se as chances do usuario acabarem, o loop quebra e o usuario perde.
## Se o usuario acertar todas as letras com um saldo positivo de chances de jogada, então o loop quebra e o usuario ganha.

from engine_forca import *
from interacoes import *

wins = 0
while True:
    user = menu(wins)
    quit(user)
    if user.strip().lower()[0] in "123":
        user = int(user)
        carregar()
        wins += start_game(user) 
    else:
        print("OPÇÃO \033[1;31mINVALIDA\033[0;0m!")
        carregar()
