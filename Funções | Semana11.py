from random import randint
import os
#sorteio
def novo(n1, n2):
     nums = []
     while (len(nums) < 6):
          num = randint(n1, n2)
          if (num in nums) == False:
               nums.append(num)

     return nums 

#contido
def contido(n, lista):
    if (n in lista):
        return '\nLegal! O número está contido na lista'
    else:
        return '\nInfelizmente, o número não está contido na lista.'

#verificar
def verificar(l1, l2):
    
    qtde = 0
    for i in range(len(l1)):
        if l1[i] in l2:
            qtde += 1
    return qtde

#cntd/inserir
def cntd(n, lista):
    if (n in lista):
        return True
    else:
        return False
def inserir(n, lista):
    n = int(input('Insira um número:')) 
    while (cntd(n, lista) == True):
        n = int(input('\n\nEsse já está contido nela! \n\nInsira outro, por favor:'))
    else:
       lista.append(n)

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
