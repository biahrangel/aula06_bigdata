# crie um algoritmo que solicite um numero ao usuario e informe o dobro, triplo e o quadrado desse numero 
# o programa devera repetir 5 vezes, permitindo que um novo numero seja informado a cada repeticao


for i in range(5):
    numero  = float (input('\ndigite um numero: '))  
    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2
    print (f'o dobro é: {dobro}')
    print (f'o triplo é: {triplo}')
    print (f'o quadrado é: {quadrado}')
 


