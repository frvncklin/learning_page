from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep='\n')

# def discount_10(a):
#     return round(a - (a * 0.10), 2)

def make_discount(value, percentage):
    return round(value - (value * percentage), 2)

discount_10 = partial(make_discount, percentage=0.10)

# A partial, basicamente, cria uma closure! Isso é incrível.

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_produtos = [
#     {**produto, 'preco': discount_10(produto['preco']) if produto['preco'] > 60 else produto['preco']}
#     for produto in produtos
# ]

def change_product_price(product, discount_function):
    return {**product, 'preco': discount_function(product['preco']) if product['preco'] > 60 else product['preco']}


novos_produtos = list(map(
    partial(change_product_price, discount_function=discount_10),
    produtos
))

# Usando list no início da declaração desse map, eu torno esse objeto em uma lista reutilizável.

# Como visto, podemos fazer o mapemaneto com list comprehension.
print_iter(novos_produtos)
print(novos_produtos)
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))
# Como os dois são True, ou seja, esse map object é um iterator.

# Lembrar também: todo generator é um iterator, mas nem todo iterator é um generator.

def is_even(number):
    if number % 2 == 0 and number != 0:
        return True
    return False

even_numbers = (x for x in range(1000000) if is_even(x))

def print_gen(gen):
    while True:
        try:
            gen_iter = iter(gen)
            print(next(gen_iter), end=', ')
        except StopIteration:
            print('END')
            break

print_gen(even_numbers)

from types import GeneratorType

print(isinstance(even_numbers, GeneratorType))

print(list(map(
    lambda x : x * 3,
    [1, 2, 3, 4]
    )))

# Se não nos importarmos em converter o valor para uma lista, ele será um iterator e, portanto, esgotável.

