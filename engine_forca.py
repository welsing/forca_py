## O pc vai sortear uma palavra e iniciar o jogo, a cada loop o usuario vai digitar uma letra ou um comando para sair
## A cada iteração uma função vai verificar se o usuario já achou todas as letras 
## e verificar se o usuario tem chances ainda para jogar.
## Se as chances do usuario acabarem, o loop quebra e o usuario perde.
## Se o usuario acertar todas as letras com um saldo positivo de chances de jogada, então o loop quebra e o usuario ganha.
from random import randint
from time import sleep
import sys
def gerar_Palavra(classe):
	'''Randomiza uma palavra por classe selecionada. \n (int) -> str'''
	animais = ['Abelha', 'Alce', 'Barata', 'Borboleta', 'Cachorro', 'Coelho', 'Elefante', 'Gato', 'Girafa', 'Hamster',
               'Iguana', 'Jacaré', 'Leão', 'Macaco', 'Ovelha', 'Panda', 'Pinguim', 'Rato', 'Tartaruga', 'Urso']
			   
	cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador", "Fortaleza", "Recife", "Curitiba",
	"Porto Alegre", "Manaus", "Belém", "Goiânia", "Vitória", "Natal", "João Pessoa", "Florianópolis", "Cuiabá",
	"Campo Grande", "Teresina", "Aracaju"]
	
	objetos = ['cadeira', 'caneta', 'chave', 'copo', 'relógio', 'telefone', 'óculos', 'livro', 'computador', 'guarda-chuva',
	'bola', 'sapato', 'garrafa', 'tesoura', 'lápis', 'faca', 'controle remoto', 'carteira', 'chapéu', 'escova de dentes']
	if classe == 1:
		return animais[randint(0, len(animais))]
	if classe == 2:
		return cidades[randint(0, len(cidades))]
	if classe == 3:
		return objetos[randint(0, len(objetos))]
	return None


def esconder_Palavra(palavra):
	'''Esconde as letras de uma palavra. \n (str) -> str'''
	hide = ""
	#tamanho = len(palavra)
	for i in range(0, len(palavra)):
		if palavra[i] != " ":
			hide += "_"
		else:
			hide += " "
	return hide


def verificar_Letra(palavra, letra):
	'''Verifica se a letra está na palavra. \n (str, str) -> bool'''
	letra = letra.lower()
	palavra.lower()
	if letra in palavra:
		return True
	else:
		return False
    
    
def mostrar_Letra(p_oculta, p_original, letra):
	'''Insere, caso haja, a letra na palavra oculta. \n (str, str, str) -> str'''
	p_original = p_original.lower()
	p_oculta = p_oculta.lower()
	letra = letra.lower()
	new = ''
	for i in range(0, len(p_original)):
		if letra == p_original[i]:
			new += letra
		else:
			new += p_oculta[i]
	return new

def carregar(chave='CARREGANDO', temp=3):
	print(chave)
	sleep(temp)


def quit():
    carregar('FECHANDO', 4)
    sys.exit()












