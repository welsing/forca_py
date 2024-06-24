from engine_forca import *
from time import sleep

def start_game(classe):
    """Inicia o jogo da forca na classe determinada e torna se venceu ou não. (int) -> int"""
    word = gerar_Palavra(classe)
    hide = esconder_Palavra(word)
    erros = []
    chances = 7
    while True:
        print("\n"*150)
        if hide.lower() == word.lower():
            print("\033[1;33mPARABÉNS!!!\033[0;00m")
            sleep(0.5)
            print(f"VOCÊ \033[1;32mACERTOU\033[0;0m A PALAVRA \033[1;32m{hide.upper()}\033[0;0m!!!")
            sleep(3)
            return 1
        if chances == 0:
            morte()
            print(f"- Você não \033[1;31mconseguiu acertar a palavra \033[1;31m{word.upper()}\033[0;0m")
            
            sleep(3)
            return 0
            
        status_do_jogo(chances, hide, erros)
        chute = input("DIGITE: ").strip().lower()[0]
        quit(chute)
        sleep(0.5)
        if verificar_Letra(word, chute):
            hide = mostrar_Letra(hide, word, chute)
        else:
            if chute not in erros:
                chances -= 1
                erros.append(chute)
		

def menu(wins):
    """Mostra o menu principal no console e retorna a escolha. (int) -> str """
    while True:
        print(f"""｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡
{f"-+ \033[1;92mJOGO DA FORCA\033[0;0m +-   VITORIAS: \033[1;36m{wins}":>37}\033[0;0m\n
- Selecione a categoria que deseja:
[1] \033[1;33mAnimais\033[0;0m
[2] \033[1;33mCidades\033[0;0m
[3] \033[1;33mObjetos\033[0;0m
[x] \033[1;31mSair\033[0;0m
»»————————————————★————————————————««""")
        select = input("DIGITE: ")
        return select

def status_do_jogo(chances, hide, erradas):
    """Visualiza o estado atual do jogo"""
    boneco = [f"""
        
        ------
        |    |
             |       >>> {hide.capitalize()}   
             |       \033[1;33m{len(hide)} letras!\033[0;0m
             |
             |          
        ------------ Chances Restantes: \033[1;31m{chances}\033[0;0m
        {erradas}             
        Digite 'X' para \033[1;31msair\033[0;0m.""",
        f"""

        ------
        |    |
             O       >>> {hide.capitalize()}   
             |       \033[1;33m{len(hide)} letras!\033[0;0m
             |
             |          
        ------------ Chances Restantes: \033[1;31m{chances}\033[0;0m
        {erradas}
        Digite 'X' para \033[1;31msair\033[0;0m.""",
        f"""

        ------
        |    |
             O       >>> {hide.capitalize()}   
            /|\\      \033[1;33m{len(hide)} letras!\033[0;0m
             |
             |          
        ------------ Chances Restantes: \033[1;31m{chances}\033[0;0m
        {erradas}
        Digite 'X' para \033[1;31msair\033[0;0m.""",
        f"""

        ------
        |    |
             O       >>> {hide.capitalize()}   
            /|\\      \033[1;33m{len(hide)} letras!\033[0;0m
             |
            /|\\          
        ------------ Chances Restantes: \033[1;31m{chances}\033[0;0m
        {erradas}
        Digite 'X' para \033[1;31msair\033[0;0m."""]
    if len(erradas) < 3:
        if len(erradas) == 0:
            nn = len(erradas)
        else:
            nn = len(erradas)
        print(boneco[nn])
    else:
        print(boneco[3])


def morte():
    """Mostra no console um game-over """
    print("""
        GAME-OVER
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
JOGUE NOVAMENTE!      """)