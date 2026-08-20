# no laco while, o trecho de codigo da repeticao esta associado a uma condicao como no if. enquanto a condicao for verdadeira, o trechoé executado.
# quando passa a ser falsa, o bloco termina

# contador = 0
# while contador < 5:
   # print ('python')
   # contador = contador + 1


#contador = 0
#while contador < 5:
    # contador = contador + 1
   # print (contador)
 #resposta = 'S'
 #while resposta == 'S':
    num = float (input('\ninforme um valor: '))
    print (f'o valor de 20% é {num * 0.2}')
    
    resposta = input('quer continuar? [S/N] ').upper()[0]
    print(resposta)
 #resposta = 'S'


 while resposta != 'N': 
    num = float (input('\ninforme um valor: '))
    print (f'o valor de 20% é {num * 0.2}') 
    resposta = input('quer continuar? [S/N] ').upper()[0]
    print(resposta)