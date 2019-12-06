#Exercício 1:

"""

def triangulo (ordem):

    for i in range(ordem + 1):
        for j in range(i):
            print(i, end=' ')

        print()
    print()

num = int(input('Digite o número de linhas do seu triangulo: '))

triangulofinal = triangulo(num)

""

#Exercício 2:

def triangulo2 (ordem):

    for i in range(num + 1):
        for j in range(i):
            print(j + 1, end=' ')

        print()


num = int(input('Digite o número de linhas do seu triangulo: '))

triangulofinal = triangulo2(num)


""


#Exercício 3:

def soma (arg1, arg2, arg3):

    adicao = arg1 +arg2 +arg3

    return adicao

num = str(input('Digite 3 números: '))

listaNum = num.split()

resultado = soma(int(listaNum[0]), int(listaNum[1]), int(listaNum[2]))

print(resultado)


""


#Exercício 4:

def neutro (num):

    if num > 0:

        return('Positivo')

    if num < 0:

        return ('Negativo')

    if num == 0:

        return('Neutro')


num = int(input('Digite um número: '))

neutralidade = neutro(num)

print(neutralidade)


""

#Exercício 5:


def somaImposto(taxaImposto, precoProduto):

    precoProduto += taxaImposto*precoProduto/100

    return precoProduto

taxa = float(input('Digite a taxa do produto em %: '))
preco = float(input('Digie o preço do produto: '))

precoFinal = somaImposto(taxa, preco)

print(precoFinal)


""

#Exercício 6:

def conversor24 (hora):

    hora -= 12

    return hora

while True:

    hora = int(input('Digite as horas: '))

    if hora == 25:
        break

    min = int(input('Digite os minutos: '))

    if hora > 12:

        horario = conversor24(hora)

        print(f'{horario}:{min} P.M')

    elif hora == 12:

        print(f'{hora}:{min}')

    else:

        print(f'{hora}:{min} A.M')



""


#Exercício 7:

cont = 0
soma = 0

def valorPagamento(valor, atraso):


    if atraso == 0:

        return valor

    else:

        valor += valor*((0.03+(0.01*atraso))/100)

        return valor

while True:

    preco = int(input('Digite o preco da prestação: '))

    if preco == 0:

        break

    dias = int(input('Digite quantos dias a prestação está atrasada: '))

    cobranca = valorPagamento(preco, dias)
    soma += cobranca
    cont += 1

    print(f'{cobranca} R$')

print(f'Foram pagas {cont} prestações, no valor total de {soma} R$')


""

#Exercício 8:

def tamanho (tamanho):

    return (len(str(tamanho)))

num = int(input('Digite um número: '))

tamanhoNum = tamanho(num)

print(tamanhoNum)


""

#Exercício 9:

def reverse (num):

    return (str(num)[::-1])


numero = int(input('Digite um número: '))

contrario = reverse(numero)

print()
print(contrario)



""

# Exercício 10:

from random import randint

listaDados = []


def craps(dados):

    if (dados == 7 or dados == 11) and len(listaDados) == 0:

        listaDados.append(dados)

        return 'Winner'

    elif (dados in listaDados):

        listaDados.append(dados)

        return 'Winner'

    elif (dados == 2 or dados == 3 or dados == 12) and len(listaDados) == 0:

        listaDados.append(dados)

        return 'Loser'

    listaDados.append(dados)


while True:

    dado = randint(2, 12)

    resultado = craps(dado)

    if resultado == 'Winner' or resultado == 'Loser':
        print(f'{resultado} {listaDados}')

        break


""

#Exercício 11:


def data (mes):

    if mes == 1:

        return 'Janeiro'

    elif mes == 2:

        return 'Fevereiro'

    elif mes == 3:

        return 'Março'

    elif mes == 4:

        return 'Abril'

    elif mes == 5:

        return 'Maio'

    elif mes == 6:

        return 'Junho'

    elif mes == 7:

        return 'Julho'

    elif mes == 8:

        return 'Agosto'

    elif mes == 9:

        return 'Setembro'

    elif mes == 10:

        return 'Outubro'

    elif mes == 11:

        return 'Novembro'

    elif mes == 12:

        return 'Dezembro'

while True:

    dia = int(input('Digite o dia da sua data: '))
    mes = int(input('Digite o mês da sua data: '))
    ano = int(input('Digite o ano da sua data: '))

    if(0 < mes <= 12) and (0 < dia <= 31):

        if ano % 4 == 0:

            if ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)) and (dia <= 31):

                datafinal = data(mes)
                print(f'Dia {dia}, de {datafinal} de {ano} é uma data válida.')
                break

            elif ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and (dia <= 30):

                datafinal = data(mes)
                print(f'Dia {dia}, de {datafinal} de {ano} é uma data válida.')
                break

            elif (mes == 2) and (dia <= 29):

                datafinal = data(mes)
                print(f'Dia {dia}, de {datafinal} de {ano} é uma data válida.')
                break

            else:

                datafinal = data(mes)
                print(f'Dia {dia}, de {datafinal} de {ano} é inválida.\nDigite uma nova data ')

        elif ano % 4 != 0:
            if ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)) and (dia <= 31):

                datafinal = data(mes)
                print(f'Dia {dia}, de {datafinal} de {ano} é uma data válida.')
                break

            elif ((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)) and (dia <= 30):

                datafinal = data(mes)
                print(f'Dia {dia}, de {datafinal} de {ano} é uma data válida.')
                break

            elif (mes == 2) and (dia <= 28):

                datafinal = data(mes)
                print(f'Dia {dia}, de {datafinal} de {ano} é uma data válida.')
                break

            else:
                datafinal = data(mes)
                print(f'Dia {dia}, de {datafinal} de {ano} é inválida.\nDigite uma nova data ')

        else:
            datafinal = data(mes)
            print(f'Dia {dia}, de {datafinal} de {ano} é inválida.\nDigite uma nova data ')

    else:
        datafinal = data(mes)
        print(f'Dia {dia}/{mes}/{ano}\nDigite uma nova data ')

""

#Exercício 12:

from random import shuffle

listaPalavra = []

def aleatorio (word):

    listaPalavra = list(word)

    shuffle(listaPalavra)

    result = ''.join(listaPalavra)

    return result.upper()

palavra = str(input('Digite uma palavra: '))

misturinha  = aleatorio(palavra)

print(misturinha)

""

#Exercício 13:

def gerar_matriz(n_linhas, n_colunas):
    matriz = []

    for k in range(n_linhas):
        matriz.append([0] * n_colunas)

    return matriz


while True:

    linhas = int(input('Digite a quantidade de linhas da matriz: '))
    colunas = int(input('Digite a quantidade de colunas da matriz: '))

    if 1 <= linhas <= 20 and 1 <= colunas <= 20:

        break

matriz = gerar_matriz(linhas, colunas)

for i in range (linhas):
    for j in range (colunas):
        if i == 0:

            matriz[i][j] = '_'

        elif i == linhas -1:

            matriz[i][j] = '_'

        elif j == 0:

            matriz[i][j] = '|'

        elif j == colunas -1:

            matriz[i][j] = '|'

        else:
            matriz[i][j] = ' '

for i in range (linhas):
    print()
    for j in range (colunas):
        print(matriz[i][j],end=' ')

"""

#Exercício 14:


from random import randint

cont = 0
listaMatrizes = []

def gerar_matriz(n_linhas, n_colunas):
    matriz = []

    for k in range(n_linhas):
        matriz.append([0] * n_colunas)

    return matriz

while len(listaMatrizes) < 8:

    cont += 1

    ordem = 3

    matriz = gerar_matriz(3,3)

    for i in range (3):
        for j in range (3):
            while True:
                aleatorio = randint(1,9)
                if aleatorio not in matriz[0] and aleatorio not in matriz[1] and aleatorio not in matriz[2]:

                    matriz[i][j] = aleatorio
                    break

    if matriz[0][0] + matriz[1][0] + matriz[2][0] == matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2] == matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] +matriz[2][1] + matriz[2][2] == matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0]:
        if matriz not in listaMatrizes:
            listaMatrizes.append(matriz)
            for i in range(3):
                print()
                for j in range(3):
                    print(f'{matriz[i][j]}',end=' ')

            print()

print(listaMatrizes)
print(cont)