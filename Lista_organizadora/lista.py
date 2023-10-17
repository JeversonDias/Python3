lista = []
dados = input('ESCREVA : ')
lista.append(dados)
lista.sort()

while dados != '':
    dados = input('ESCREVA : ')
    lista.append(dados)
    lista.sort()

with open('lista.txt', 'a', encoding='UTF-8') as arquivo:
    for item in lista:
        arquivo.write(item + '\n')
