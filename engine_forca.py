
from random import randint
from time import sleep
import sys
def gerar_Palavra(classe):
	'''Randomiza uma palavra por classe selecionada. \n (int) -> str'''
	animais = ['Abelha', 'Alce', 'Barata', 'Borboleta', 'Cachorro', 'Coelho', 'Elefante', 'Gato', 'Girafa', 'Hamster',
               'Iguana', 'Jacare', 'Leao', 'Macaco', 'Ovelha', 'Panda', 'Pinguim', 'Rato', 'Tartaruga', 'Urso']
			   
	cidades = ["Sao Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasilia", "Salvador", "Fortaleza", "Recife", "Curitiba",
	"Porto Alegre", "Manaus", "Belem", "Goiania", "Vitoria", "Natal", "Joao Pessoa", "Florianopolis", "Cuiaba",
	"Campo Grande", "Teresina", "Aracaju"]
	
	objetos = ['cadeira', 'caneta', 'chave', 'copo', 'relogio', 'telefone', 'oculos', 'livro', 'computador', 'guarda-chuva',
	'bola', 'sapato', 'garrafa', 'tesoura', 'lapis', 'faca', 'controle remoto', 'carteira', 'chapeu', 'escova de dentes']
	if classe == 1:
		return animais[randint(0, len(animais)-1)]
	if classe == 2:
		return cidades[randint(0, len(cidades)-1)]
	if classe == 3:
		return objetos[randint(0, len(objetos)-1)]
	return None


def esconder_Palavra(palavra):
	'''Esconde as letras de uma palavra. \n (str) -> str'''
	hide = ""
	for i in range(0, len(palavra)):
		if palavra[i] != " ":
			hide += "_"
		else:
			hide += " "
	return hide


def verificar_Letra(palavra, letra):
	'''Verifica se a letra está na palavra. \n (str, str) -> bool'''
	letra = letra.lower()
	palavra = palavra.lower()
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
	"""Simula um carregamento para causar mais imersão no game"""
	print(chave)
	sleep(temp)


def quit(x):
	"""Fecha o programa"""
	if x == "x":
		carregar('FECHANDO', 4)
		sys.exit()












