#TIPOS DE DADOS

#str = 'Marco'          / string
#int = 1                / inteiro
#float = 1.2            / real
#bool = True / False    / booleano


#CONVERSÃO PARA NUMERO INTEIRO
n1 = int(input('Digite um numero'))

#CONVERSÃO PARA NUMERO REAL
n2 = float(input('Digite um numero'))

#CONCATENAÇÃO / duas maneiras diferentes
soma1 = 1 + 2
print('A soma vale {}' .format(soma1))

soma2 = 2 + 4
print('A soma vale', soma2)

#EXERCICIO
number1 = int(input('Digite um numero'))
number2 = int(input('Digite outro numero'))
soma = number1 + number2

print('A soma entre {} e {} é {}'.format(number1, number2, soma))
# ou print('A soma entre', number1, 'e', number2, 'é:', soma)


#TESTE DE TIPO
teste = input('Digite algo')
print(teste.isalpha)
            #isnumeric = O valor da variável é numero ?
            #isdecimal = .. é decimal ?
            #issuper =  .. é maiusculo ?
            #islower = .. é minusculo ?
            #...