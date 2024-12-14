
#Objetivo: Mostrar o numero passado pelo usuário e seu antecessor e sucessor.

numero = int(input('digite um numero'))
antecessor = numero - 1
sucessor = numero + 1

print('Antecessor: {} Numero: {} Sucessor: {}'.format(antecessor, numero, sucessor))