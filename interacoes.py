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
            print("PARABÉNS!!!")
            sleep(0.5)
            print(f"VOCÊ ACERTOU A PALAVRA {hide.upper()}!!!")
            sleep(3)
            return 1
        if chances == 0:
            morte()
            print(f"- Você não conseguiu acertar a palavra {word.upper()}")
            
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
{f"-+ JOGO DA FORCA +-   VITORIAS: {wins}":>37}\n
- Selecione a categoria que deseja:
[1] Animais
[2] Cidades
[3] Objetos
[x] Sair
»»————————————————★————————————————««""")
        select = input("DIGITE: ")
        return select

def status_do_jogo(chances, hide, erradas):
    """Visualiza o estado atual do jogo"""
    boneco = [f"""
        
        ------
        |    |
             |       >>> {hide.capitalize()}   
             |       {len(hide)+1} letras!
             |
             |          
        ------------ Chances Restantes: {chances}
        {erradas}             
Digite 'X' para sair.""",
        f"""

        ------
        |    |
             O       >>> {hide.capitalize()}   
             |       {len(hide)+1} letras!
             |
             |          
        ------------ Chances Restantes: {chances}
        {erradas}
Digite 'X' para sair.""",
        f"""

        ------
        |    |
             O       >>> {hide.capitalize()}   
            /|\\      {len(hide)+1} letras!
             |
             |          
        ------------ Chances Restantes: {chances}
        {erradas}
Digite 'X' para sair.""",
        f"""

        ------
        |    |
             O       >>> {hide.capitalize()}   
            /|\\      {len(hide)+1} letras!
             |
            /|\\          
        ------------ Chances Restantes: {chances}
        {erradas}
        Digite 'X' para sair."""]
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