# uma instituicao de ensino precisa calcular a media dos alunos. crie um algoritmo que para cada aluno, solicite 4 notas
# calcule a media e informe o resultado 
# se a media for maior ou 7, o algoritmo deve imprimir "estudante aprovado"
# o programa devera repetir esse processo p/ 10 alunos, permitindo informar as notas de cada aluno durante a execucao. 

for i in range (10):
    print(f'\nALUNO {i+1}') #para aparecer o numero do aluno, com esse i + 1 ele vai aumentando os numeros e comeca do 1
    nota1 = float (input('\nDigite a nota 1: '))
    nota2 = float (input('Digite a nota 2: '))
    nota3 = float (input('Digite a nota 3: '))
    nota4 = float (input('Digite a nota 4: '))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >=7: 
        print(f'a nota final foi: {media}, estudante aprovado')
    else:
        print(f'a nota final foi: {media}, estudante reprovado')
