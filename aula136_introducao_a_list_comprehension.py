# Nesta aula vamos começar a tratar de list comprehension.

# Vamos começar com um exemplo básico:

# A list comprehension é algo que o Python faz por debaixo dos panos.

# print(list(range(10)))

# Vamos declarar uma lista, filtrar e fazer condicionais, tudo em uma mesma linha.

list = [number * 2 for number in range(10) if (number * 2) != 16]

print(list)

# É tipo isso.

# A esquerda do for, colocamos o que queremos incluir na lista, na direita fazemos o filtro.
# Eu acho que é explicitamente preciso que ambos os lados estejam falando sobre a mesma coisa.
