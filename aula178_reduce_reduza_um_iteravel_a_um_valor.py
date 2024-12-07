from aula177_filter_um_filtro_funcional import produtos, print_iter

print_iter(produtos)

# reduce reduz um iterável em um único valor.
# ela vem com o Python mas não está na linguagem.

from functools import reduce

# Atenção, pois esa função pode ser complicada.

total = 0
for produto in produtos:
    total += produto['preco']

# Ou

total = sum([product['preco'] for product in produtos])

print(round(total, 2))

# Nesse caso, a nossa variável 'total' é um *acumulador*.

# A função reduce precisa de um acumulador.

def funcao_do_reduce(acumulador, item):
    return acumulador + item

total = reduce(
    lambda acumulator, product: acumulator + product['preco'],
    # A função do reduce recebe, sempre, o acumulador e 
    # Pelo que eu entendi, o reduce está colocando como argumentos nessa função o acumulador e o iterável,
    # respectivamente.
    # A cada next do iterator de produtos, ele vai aplicar essa função, guardando o valor do acumulador.
    produtos,
    0   # Valor inicial. Sempre inicar com o valor inicial.
)

print(round(total, 2))

def reduce_na_mao(funcao, iterable, valor_inicial):
    iterator = iter(iterable)
    acumulador = valor_inicial
    while True:
        try:
            proximo = next(iterator)
            acumulador = funcao(acumulador, proximo)
        except StopIteration:
            break
    return acumulador
            
numeros = [1, 2, 3, 4, 6]

def soma(x, y):
    return x + y

print(reduce_na_mao(soma, numeros, 0))