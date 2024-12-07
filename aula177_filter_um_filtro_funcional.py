def print_iter(iterator):
    print(*list(iterator), sep='\n')

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

produtos.sort(key=lambda product: product['nome'])

novos_produtos = filter(
    lambda product: product['preco'] > 60,
    # Se essa condição retornar False, meu elemento não será incluído. Se retornar True, aí sim ele será 
    # incluído.
    produtos
)

print_iter(novos_produtos)

# Os parâmetros do map e do filter são passados por meio de funções.