from funções import contido, inserir, novo, contido, verificar, inserir, limpar

print('','==' * 42,'\n      Aqui vai um sorteio aleatório pra você.\n      Seis números aleatórios, mas menores que 100:','\n','==' * 42,'\n\n\nSorteando...\n\n\n')
print(novo(0, 99))
input('Aperte <enter> para continuar ...')
limpar()


print('\n\n\n', '==' * 42,'\n   Agora, vamos verificar se um número que você disser estará contido numa lista!\n','==' *42)
print('\nCá comigo, tenho uma lista de 10 números.')
print()
n = int(input('Digite um número, por favor: '))
lista =[1, 2, 3, 6, 7, 14, 21, 42]

print(contido(n, lista))
print(f'\nOlha só ela aqui: {lista}')
input('Aperte <enter> para continuar ...')
limpar()

print('\n\n\n', '==' * 42,'\n   Beleza! Agora é o seguinte:\n   Você irá definir 2 listinhas pra mim.\n   Em contrapartida, eu vou te dizer quantos elementos da lista 1 estão na lista 2.\n','==' *42)

l1 = [] * 5
l2 = [] * 5
print()
print('Você inserirá 5 números, distintos ou não, em 2 listas diferentes.\n\nEu vou verificar e te dizer a quantidade de números da primeira lista contida na segunda.')
print('\n')
print('Esta será nossa lista 1. ')

for l in range(0, 5):
     l1.append(int(input('Digite um número: ')))

print('\n')
print('Maravilha! Vamos agora a nossa lista 2. ')
print('\n')

for l in range(0, 5):
     l2.append(int(input('Digite um número: ')))
print()
print(l1)
print()
print(l2)
print('\n\nMuito bem! \n\n\nVerificando...\n\n\n')
print('A quantidade de números da lista 1 contidos na lista 2 é:', end=' ')
print(verificar(l1, l2))
input('Aperte <enter> para continuar ...')
limpar()

print('\n\n\n', '==' * 42,'\n      Por último, terei uma lista aqui e você digitará um número. \n      Se ele já não estiver na lista, eu vou inserí-lo pra você. ;)   ','\n', '==' *42)

numeros = [0, 42, 84, 126, 168, 210, 252, 294, 336, 378, 420]
n = inserir(5, numeros)
print('\n\n\nMuito bem!!! Aqui está a lista como seu novo número digitado:\n\n ', numeros, '\n')

print('\n')
input('Aperte <enter> para continuar ...')
limpar()
print('\n\n\n', '==' * 24,'\n       Muito obrigado por participar. \n\n            Até mais!!! ;D   ','\n', '==' *24)

