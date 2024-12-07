# Podemos fazer list comprehensions com vários for's.

# lista = []

# for x in range(3):
#     for y in range(3):
#         lista.append((x, y))

# lista = [(x + 1, y + 1) for x in range(10) for y in range(3)]

# print(lista)

# Pelo que concluí, basta fazer exatamente o que fizemos acima.

# Lembrar sempre da estrutura: mapeamento - lógica - filtro.

# As list comprehensions fazem a mesma coisa que as funções map, filter,
# flatmap e mais.

# A list comprehension permite com que eu, baseado em um iterável, gere
# outro iterável e consigo fazer nesse meio um processamento de dados.

# --- Notas da Aula do Youtube ---

# Quando atribuímos a uma variável o valor de outra variável, geralmente
# Não copiamos o valor, e sim apontamos para o mesmo local na memória.

numeros = [1, 2, 3, 4, 5]
# novos_numeros = numeros

# novos_numeros[0] = 20
# print(numeros)

# Uma shallow copy copia todos os valores IMUTÁVEIS de uma lista.

# novos_numeros = numeros.copy()  # Isso é uma shallow copy.

# novos_numeros = [numero for numero in numeros]  # Isso também é uma cópia.

# Isso equivale a :

# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)

# Por que utilizar list comprehension?

# novos_numeros = [(numero / 2) for numero in numeros]
# novos_numeros = [(numero * 2) for numero in numeros]
# novos_numeros = [(numero ** 2) for numero in numeros]

# numeros[0] = 20

# print(numeros)
# print(novos_numeros)

# Dê preferência para codar em inglês.

# O map pega tudo o que está em uma lista e joga para outra lista,
# sendo que nós podemos processar estes dados.

# Já quando a gente faz o filter, eliminamos alguns itens.

def is_prime(number):
    if number in (0, 1):
        return False
    for i in range(number):
        if i in (0, 1):
            continue
        elif number % i == 0:
            return False
    return True

def is_uneven(number):
    if number % 3 == 0 and number not in (0, 1):
        return True
    return False

def is_even(number):
    if number % 2 == 0 and number not in (0, 1):
        return True
    return False
        

numbers = [number for number in range(1000)]
prime_numbers = [number if number != 127 else f"Target: {number}" for number in numbers if is_prime(number)]
uneven_numbers = [number for number in numbers if is_uneven(number)]
even_numbers = [number for number in numbers if is_even(number)]

print("Prime Numbers:", prime_numbers)
print()
print("Uneven Numbers:", uneven_numbers)
print()
print("Even Numbers:", even_numbers)

# Basicamente, o mapeamento pega todos os itens da lista e transfere para
# A outra lista, transformando um, mais ou todos os itens ao fazer a 
# tranferência.