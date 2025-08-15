#Crie um dicionário para armazenar o nome e o preço de cinco produtos. Peça ao usuário para inserir o nome de cada produto e o respectivo preço. À medida que o usuário fornece os dados, armazene cada produto como uma chave no dicionário e o preço como o valor associado a essa chave. Após a inserção de todos os produtos e preços, calcule o valor total da compra somando todos os preços armazenados no dicionário. Por fim, exiba o valor total da compra.'''

produtos ={}
valor_total_da_compra = 0

nome_produto01 = input('Digite o nome do primeiro produto: ')
produtos[nome_produto01] = preco_produto01 = float(input('Digite o preço do primeiro produto: '))
valor_total_da_compra += preco_produto01

nome_produto02 = input('Digite o nome do proximo produto: ')
produtos[nome_produto02] = preco_produto02 = float(input('Digite o preço do proximo produto: '))
valor_total_da_compra += preco_produto02

nome_produto03 = input('Digite o nome do proximo produto: ')
produtos[nome_produto03] = preco_produto03 = float(input('Digite o preço do proximo produto: '))
valor_total_da_compra += preco_produto03

nome_produto04 = input('Digite o nome do proximo produto: ')
produtos[nome_produto04] = preco_produto04 = float(input('Digite o preço do proximo produto: '))
valor_total_da_compra += preco_produto04

nome_produto05 = input('Digite o nome do proximo produto: ')
produtos[nome_produto05] = preco_produto05 = float(input('Digite o preço do proximo produto: '))
valor_total_da_compra += preco_produto05


print(f'O valor total da compra é R$: {valor_total_da_compra}')
