from engine_forca import *
from time import sleep

def start_game(classe):
    #word = gerar_Palavra(classe)
    word = "Rio de janeiro"
    hide = esconder_Palavra(word)
    erros = []
    chances = 7
    while True:
        print("\n"*150)
        if hide.lower() == word.lower():
            print("PARABÉNS!!!")
            sleep(0.5)
            print(f"VOCÊ ACERTOU A PALAVRA!!! {hide.upper()}")
            sleep(3)
            return 1
        if chances == 0:
            morte()
            print(f"- Você não conseguiu acertar a palavra {word.upper()}")
            sleep(3)
            return 0
            
        criar_bonequinho(chances, hide, erros)
        chute = input("DIGITE: ").strip().lower()[0]
        if verificar_Letra(word, chute):
            hide = mostrar_Letra(hide, word, chute)
        else:
            chances -= 1
            erros.append(chute)
		

def menu(wins):
    while True:
        print(f"""｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡
{f"-+ JOGO DA FORCA +-   VITORIAS: {wins}":>37}\n
- Selecione a categoria que deseja:
[1] Animais
[2] Cidades
[3] Objetos
[x] Sair
»»————————————★————————————««""")
        select = input("DIGITE: ")
        return select

def criar_bonequinho(chances, hide, erradas):
    boneco = [f"""

        ------
        |    |
             |       >>> {hide.capitalize()}   
             |       {len(hide)+1} letras!
             |
             |          
        ------------ Chances Restantes: {chances}
        {erradas}                        """,
        f"""

        ------
        |    |
             O       >>> {hide.capitalize()}   
             |       {len(hide)+1} letras!
             |
             |          
        ------------ Chances Restantes: {chances}
        {erradas}""",
        f"""

        ------
        |    |
             O       >>> {hide.capitalize()}   
            /|\\      {len(hide)+1} letras!
             |
             |          
        ------------ Chances Restantes: {chances}
        {erradas}""",
        f"""

        ------
        |    |
             O       >>> {hide.capitalize()}   
            /|\\      {len(hide)+1} letras!
             |
            /|\\          
        ------------ Chances Restantes: {chances}
        {erradas}"""]
    if len(erradas) == 0:
        print(len(erradas))                   ## ta imprimindo 2 bonecos ajeitar dps
        print(boneco[0])
    if len(erradas) < 3 and len(erradas) > 0:
        print(len(erradas))
        print(boneco[len(erradas)-1])
    else:
        print(boneco[3])


def morte():
    print("""
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
          """)