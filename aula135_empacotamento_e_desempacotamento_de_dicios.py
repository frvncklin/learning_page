# a, b = 1, 2 # Packing
# a, b = b, a # Unpacking


# a, b = person

# # Desempacotamos completamente o pessoa.items() assim:
# for item, key in person.items():
#     print(item, key)

# # O items() retorna uma tupla com chave e valor.

# # Dessa forma:

# (a1, a2), (b1, b2) = person.items()
# print(a1, a2)
# print(b1, b2)

# Fizemos um desempacotamento interno.

person = {
    'name': 'Gabrielle',
    'surname': 'Francklin'
}

data_person = {
    'age': 24,
    'height': 1.68
}

# Vamos juntar esses dicios:
# Para extrair os valores de um dicio, usamos dois asteriscos.

# Forma 1:

# complete_person = {
#     **person, 'chave': 1
# }

# Dessa forma, eu pego todo o conteúdo de pessoa e coloco em complete_person, mais a chave e o valor
# que digitei depois.
# Eu posso também alterar o valor das chaves existentes:

complete_person = {
    **person, **data_person, 'name': person['name'].lower()
}

# Dessa forma, eu peguei os dados de ambos os dicionários e mudei o valor da chave 'name' do dicio person.

print(complete_person)

def show_named_arguments(*args, **kwargs):
    print('Not named: ', args)

    for key, value in kwargs.items():
        print(key, value)
# Em suma, um dicionário são um conjunto de argumentos nomeados, podemos ver dessa forma.

show_named_arguments(1, 23, 'olá', name='Victor', age=32)

# kwargs precisam ser sempre desempacotados

# Quando temos uma função com muitos argumentos e não queremos passar eles 1 a 1, podemos criar um dicionário
# e desempacotar ele na função.

#Ex:

configs = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3
}

# Para passar esses argumentos para uma função, usamos:

show_named_arguments(**configs)