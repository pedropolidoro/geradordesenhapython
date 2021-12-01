from emoji import emojize
from sys import exit
from random import randint
from emoji.core import emojize
print(' ')
print('Digite o numero do seu aventureiro para escolhe-lo')
print(' ')
print('--------------------------')
print(emojize("1-Cara alegre        :smiley:", use_aliases=True))
print('--------------------------')
print(emojize("2-Cara triste        :cry:", use_aliases=True))
print('--------------------------')
print(emojize("3-Cara apaixonado    :heart_eyes:", use_aliases=True))
print('--------------------------')
print(emojize("4-Cara zangado       :rage:", use_aliases=True))
print('--------------------------')
print(emojize("5-Cara desconfiado   :expressionless:", use_aliases=True))
print('--------------------------')

plesc = input('--->')

if plesc == '1':
    playerchar = (emojize(':smiley:', use_aliases=True))

if plesc == '2':
    playerchar = (emojize(':cry:', use_aliases=True))

if plesc == '3':
    playerchar = (emojize(':heart_eyes:', use_aliases=True))

if plesc == '4':
    playerchar = (emojize(':rage:', use_aliases=True))

if plesc == '5':
    playerchar = (emojize('expressionless:', use_aliases=True))

#MENSAGEM DE BOAS VINDAS

print('')
print('Olá {}, como deseja ser chamado?'.format(playerchar))
pname = input('---> ')
print('')
print('Olá {}, seja bem vindo ao jogo da advinhacão'.format(pname))
print('Nesse jogo, eu darei um numero, e voçê tera que acerta-lo, se acertar vc ganha oa game')
print('')
print('Deseja começar? (s/n)')
startq = input('---> ')
if startq == 'n':
    print('{}, tem certeza que quer abandonar o jogo? (s/n)'.format(pname))
    qtgameq = input('--->')
    if qtgameq == 's':
        exit()
if startq == 's':
    print('')
    print('Então vamos começar! Digite um numero entre 0 e 5')
    print('')
    cdnm = int(input('Digite seu numero aqui ---> '))
if cdnm > 3:
    print('Parabens {}, você ganhou o jogo, sua recompensa esté em: encurtador.com.br/kmvyS '.format(pname))
if cdnm < 4:
    print('Infelizmente não ganhastes o jogo, tente novamente')