print('~' *42)
print('            Testemos Funções!!!')
print('~' *42)

#Programa Divisores / É primo?
 
def divisores(n):
    for d in range(1, n + 1):
        if n % d == 0:
            print(d)

def primo(n):
    contador = 0

    for i in range(1, n + 1):
        if n % i == 0:
            contador += 1
    print("O número {} foi divisível {} vezes!".format(n, contador))
    if contador == 2:
        print("Portanto, ele é primo")
    else:
        print("E por isso ele não é primo")
    


n = int(input('Digite um número e eu vou te falar os divisores dele: '))
divisores(n)


print('~' *84)
print('            Ótimo!!! Agora, vamos verificar se esse número é primo!')
print('~' *84)
print('\n')
print('Verificando...')
print('\n')
primo(n)
print('\n')

# Exibir o menor valor de uma lista

print('~' *84)
print('        Muito bem! Agora vamos definir o menor valor de uma pequena lista! ')
print('~' *84)
print(' ')

def menor(lista):
    men = 0
    mai = 0
    for c in range(0, 5):
        lista.append(int(input(f'Digite um valor para a posição {c}: ')))
        if c == 0:
            mai = men = lista[c]
        else:
            if lista[c] > mai:
                mai = lista[c]
            if lista[c] < men:
                men = lista[c]
    print('\n')
    print('Verificando...')
    print('\n')
    print(f'Dos valores digitados, o menor é o número {men}')
    print('\n')

lista = []

menor(lista)

#Calculando o número de caracteres especiais numa frase

print('~' *84)
print(' Mudando de assunto, que tal calcular quantos caracteres especiais há em uma string? ')
print('~' *84)
print(' ')
print('HAHAHA! Pensou que NÃO era uma resposta válida? Bobinho...')
print()

def especial(st):
    qtde = 0
    for c in st:
        if (not (c >= '0' and c <= '9') and
            not (c >= 'A' and c <= 'Z') and
            not(c >= 'a' and c <= 'z')):
            qtde += 1
    return qtde

frase = input('Agora, me diga uma frase qualquer: ')
print('\n')
print('Verificando...')
print('\n')
print('O número de caracteres especiais nesta frase é de: ', end='')
print(especial(frase), '\n')

#Verificando se os números de uma lista são distintos

print('~' *63)
print('        Por último, me dê uma pequena lista de números \n        e eu lhe direi se eles são distintos entre si. ')
print('~' *63)
print('\n')

def distintos(lista):
    t = len(lista)
    for i in range(t):
        if (lista[i] in lista[i + 1 : t]):
            return '\nHá repetições nos números desta lista\n'
    return '\nÓtimo! Todos os números desta lista não distintos entre si\n.'

numeros = eval('[' + input('Por favor, digite uma lista de números \nserparados com vírgula: ') + ']') 

print(distintos(numeros))

print('~' *63)
print('        Obrigado! É isso aí. Te vejo na próxima. \n        Agora você e sua família estão livres! ;D')
print('~' *63)
print('\n')
