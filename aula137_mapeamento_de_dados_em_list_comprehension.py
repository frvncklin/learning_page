# Vamos falar sobre o mapeamento de dados em List comprehension.

# Na programação funcional, existe uma função chamada Map usada justamente para isso.

list = [number * 2 for number in range(10) if (number * 2) != 16]

print(list)

# O map pegar um índice para o outro. 
# O map pega os dados de um lado do iterável, transforma eles ou não e joga no outro lado.
# Neste caso, ambos os iteráveis tem o mesmo tamanho. 

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

def desconto_10(item):
    return item - (item * 0.10)

# O mapeamento meio que pega os dados, transforma e joga em outro lugar.

novos_produtos = [{**produto, 'preco': desconto_10(produto['preco'])} for produto in produtos]

# Neste caso, está explicíto que estamos criando uma nova lista de dicionários usando os kwargs do dicionário 
# produtos. Além disso, como podemos alterar ou criar novas chaves no ato do desempacotamento,
# estamos aproveitando para modificar os valores das chaves 'preco' em cada produto.

print(*novos_produtos)