'''

                #EXERCÍCIOS DE PYTHON

#VARIÁVEIS
nome = 'Marco'
idade = 24

#IMPRIMIR NA TELA
nome = input('Qual é o seu nome?')
print('Olá', nome)

#EXERCICIO
#OBJETIVO: CALCULAR SALÁRIO HORA
valor_salario = int(input('Qual o seu salário?'))
horas = int(input('Quantas horas no mês?'))
valor_hora = valor_salario / horas

print('O valor do salario hora deste funcionário é {}'.format(valor_hora))



#CONDICIONAIS: if(se), else(se não) e elif(se não, se)

#Exemplo 1
trabalho_terminado = True
if trabalho_terminado == True:
    print('Posso sair')
else:
    print('Não posso sair')

    
#Exemplo 2
estar_livre = False

if estar_livre == True:
    print('Posso te ajudar')
else:
    print('Não posso ajudar')


#Exemplo 3
numero_de_atraso = 3

if numero_de_atraso >= 3:
    print('Você está suspenso')
elif numero_de_atraso == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atraso == 2:
    print('Pode entrar, porém caso tome mais 1 falta, irá ser suspenso')


#Exemplo 4
primeiro_valor = 7
segundo_valor = 7

if primeiro_valor > segundo_valor:
    print('O primeiro numero é maior')
elif primeiro_valor < segundo_valor:
    print('O segundo número é maior')
else:
    print('Os números são iguais')


#Exemplo 5
hora_do_dia = 'Manhã'

if hora_do_dia == 'Manhã':
    print('Bom dia!')
elif hora_do_dia == 'Tarde':
    print('Boa tarde!')
elif hora_do_dia == 'Noite':
    print('Boa noite!')
'''
'''
#LAÇOS DE REPETIÇÃO + LISTAS

for item in range(1,21):  # 1 à 20
    print(item)

for item in range(1,21,2): # 1 à 20 (2 em 2)
    print(item)

'''
nomes = ['Marco', 'Ana', 'Marcela', 'Maria', 'Julia']
for nome in nomes:
    print(nome)

lista_produtos = ['notbook', 'ipad', 'celular']
for produto in lista_produtos:
    print(produto)

'''
#Exercicio
valor_maximo = int(input('Digite o valor máximo'))
valor_inicial = 1

for numero in range(valor_inicial, valor_maximo + 1):
    print(numero)
'''