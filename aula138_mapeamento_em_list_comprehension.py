def discount_10(item):
    return item - (item * 0.10)

def print_dict(dict):
    for item in dict:
        print(item)

products = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30},
]

new_products = [{**product, 'preco': discount_10(product['preco'])} if product['preco'] >= 20 else {**product} for product in products]
# Com esssa sintaxe, eu crio um novo dicionário para cada iterável.
print_dict(new_products)

# O if após o for filtra a lista toda. Todos os itens que não estiverem
# No if não serão incluídos na lista, ou seja, ele corta o circuito 
# completamente.
# Já o if antes do for filtra a condição que colocamos antes do for.
# Caso o item esteja em conformidade com a condição, ela será
# Aplicada. Caso contrário não ocorre nada e o item ainda
# será incluído.

# Códigos demasiadamente complexos não são interessantes.

