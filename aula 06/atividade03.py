# uma loja deseja registrar as vendas realizadas durante o atendimento aos clientes. Em cada venda, sao consideradas o valor unitario do produto
# e a quantidade de unidades vendidas.

# crie um algoritmo para registrar 3 vendas e apresentar o valor total de cada venda ao final de cada atendimento 

for i in range(3):
    valor_item = float (input('\nValor do item: R$ '))
    quantidade = float (input('quantidade de itens: '))
    valor_total = valor_item * quantidade 
    print(f'valor total da venda: R$ {valor_total}')