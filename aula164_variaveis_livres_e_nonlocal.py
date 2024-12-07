# def outer(number):
#     a = number
#     def inner():
#         # print(locals())
#         print(inner.__code__.co_freevars)
#         return number
#     # Como 'a' não está definida dentro do escopo da função
#     # 'inner', ela é considerada uma variável livre.
#     return inner

# number_10 = outer(10)

# print(number_10())

# Um exemplo bem besta, mas só pra testar.

# import gc

# def concatenate(initial_string):
#     final_value = initial_string
#     def add_into_final_value(added_value):
#         return final_value + added_value
#     return add_into_final_value

# good_morning = concatenate("Good Morning, ")

# list_of_names = ['Victor', 'Gabrielle', 'Dita', 'Claudia']

# list_of_greetings = [good_morning(name) for name in list_of_names]

# print(*list_of_greetings, sep='\n')


# def consecutive_additions():
#     sum = 0
#     def make_addition(add_into_sum):
#         nonlocal sum
#         sum += add_into_sum
#         return sum
#     return make_addition

# make_add = consecutive_additions()
# Fazendo isso, eu meio que salvo na memória o estado de
# uma função.
# Nós estamos slavando a execução da função em uma variável
# e deixando ela pausada ali.

# for i in range(100):
#     print(make_add(i))

# print(make_add(90))

# def is_prime(number):

#     if number not in (0, 1):
#         for i in range(2, number):
#             if number % i == 0:
#                 return False
#     return True

# def list_primes(number_of_primes):

#     def make_primes():
#         counter = 0
#         prime_number = 0

#         while counter <= number_of_primes:
#             while not is_prime(prime_number):
#                 prime_number += 1
#             yield prime_number
#             prime_number += 1
#             counter += 1

#     for prime_number in make_primes():
#         print(prime_number)

# Fiz um generator para não ocupar muita memória.

# Variáveis livre devm ser declaradas como nonlocal para 
# serem alteradas fora de seu escopo. Caso isso não seja feito
# irá ser gerado o erro UnboundLocalError.