'''Crie um dicionário para armazenar o nome e o preço de cinco produtos.
Peça ao usuário para inserir o nome de cada produto e o respectivo preço. 
À medida que o usuário fornece os dados, armazene cada produto como uma chave
no dicionário e o preço como o valor associado a essa chave. Após a inserção de 
todos os produtos e preços, calcule o valor total da compra somando todos os preços 
armazenados no dicionário. Por fim, exiba o valor total da compra.'''

produtos ={}
valor_total_da_compra = 0

for i in range(5):
    nome_produto = input('Digite o nome do produto: ')
    produtos[nome_produto] = preco_produto = float(input('Digite o preço do produto: '))
    valor_total_da_compra += preco_produto
            
print(f'O valor total da compra é R$: {valor_total_da_compra}')
