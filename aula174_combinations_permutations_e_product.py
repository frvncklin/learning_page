people = ['Gabrielle', 'Victor', 'Dita', 'Claudia', 'Roberto']

shirts = [
    ['black', 'white', 'purple', 'blue'],   # Color.
    ['S', 'M', 'L', 'XL', 'XXL'],           # Size.
    ['masculine', 'feminine', 'unissex'],   # Type.
    ['cotton', 'poliester']
]

def print_iter(iter):
    print(*list(iter), sep='\n')

from itertools import combinations, permutations, product
# Combinação - A ordem não importa.
# Permutação - A ordem importa.
# Produto - A ordem importa e repetem-se valores únicos.
print_iter(combinations(people, 2))

# print(*list(combinations(people, 2)), sep='\n')
# Melhor:
# print_iter(combinations(people, 2))

'''
Basicamente, o módulo itertools nos fornece ferramentas para
criarmos iterators.
Isso é algo muito útil e pode ser uma ferramenta poderosa.

Permutações criam toda as combinações possíveis em que a 
ordem importa.
'''

# print_iter(permutations(people, 2))
print_iter(product(*shirts))

# desempacotando shirts, temos duas listas.
# dessa forma, é possível fazer o produto cartesiano delas.
# Se passássemos apenas shirts, não seria possível desempacotar
# Pois não teríamos outro argumento para fazer o produto cartesiano.
# Da mesma forma, se shirts tivesse 3 listas dentro dela
# e fizéssemos product(*shirts), teríamos o produto cartesia-
# no das 3 listas.