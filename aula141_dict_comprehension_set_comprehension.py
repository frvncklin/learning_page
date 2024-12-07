# Tudo que poemos fazer com list comprehension pode ser 
# feito aqui também.

product = {
    'name': 'Corolla GR',
    'price': 145000,
    'category': 'sedan'
}

print(product.items())

new_product = {key: value.upper() if isinstance(value, str) else value for key, value in product.items() if key != 'category'}

print(new_product.items())

# O dict comprehension se comporta um pouco diferente da list 
# comprehension.

list = [
    ('a', 'a value'),
    ('b', 'b value'),
    ('c', 'c value'),
    ('d', 'd value')
]

new_dict_from_list = {key: value for key, value in list}
print(new_dict_from_list)

# Dá pra fazer com sets também!

s1 = {i ** 2 for i in range(40)}

print(s1)