from engine_forca import *
from interacoes import *

wins = 0
while True:
    user = menu(wins)
    if user.strip().lower()[0] in "123":
        user = int(user)
        carregar()
        wins += start_game(user)
    elif user.strip().lower()[0] == "x":
        quit()  
    else:
        print("OPÇÃO INVALIDA!")
        carregar()
