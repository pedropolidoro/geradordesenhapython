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

sleep(0.45)
print('\033[1;34m|\033[0;0m3\033[1;34m|\033[0;0m')
sleep(0.75)
print('\033[1;34m|\033[0;0m2\033[1;34m|\033[0;0m')
sleep(0.75)
print('\033[1;34m|\033[0;0m1\033[1;34m|\033[0;0m')
sleep(0.75)

print('\nA senha gerada aleatoriamente é: \033[1;31m|\033[0;0m    \033[;1m{}\033[0;0m      \033[1;31m|\033[0;0m Contendo {} caracteres no total.\n'.format(fpin, int(numeroDeCaracteresEspeciais)+int(numeroDeLetras)))
