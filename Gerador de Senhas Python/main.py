from random import choice
from string import hexdigits, punctuation
from time import sleep, time

print('\nGerador de senhas\n')

numeroDeLetras = int(input("Qual a quantidade de caracteres?\n\033[1;34m--->\033[0;0m "))
numeroDeCaracteresEspeciais = int(input("\nQual a quantidade de caracteres especiais?\n\033[1;34m--->\033[0;0m "))
letras = hexdigits
caracteresEspeciais = punctuation
caracteresGerador = ''.join(choice(letras) for _ in range(numeroDeLetras))
caracteresEspeciaisGerador = ''.join(choice(caracteresEspeciais) for _ in range(numeroDeCaracteresEspeciais))
fpin = caracteresGerador + caracteresEspeciaisGerador

print('\nGerando sua senha, aguarde\n')

sleep(2)

print('\nA senha gerada aleatoriamente é: \033[1;34m{}\033[0;0m\n'.format(fpin))
