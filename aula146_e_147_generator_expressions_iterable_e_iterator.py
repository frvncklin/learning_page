# Generator é algo específico do Python.
# Ele é algo mais novo, muito mais novo do que o iterator.

# Os generators são funções que sabem pausar.

# Iterator é uma classe que tem o método iter e o método next.

# Todo generator é um iterator, mas um iterator não é um generator.

# import sys

# list_sample = [number for number in range(200000)]
# generator = (number for number in range(200000))

# for number in generator:
#     print(number)

# # O generator não salva tudo na memória.

# print(sys.getsizeof(list_sample), sys.getsizeof(generator))
# Podemos ver que a lista ocupa 10x mais espaço que o generator.

# O generator só conhece nosso próximo valor. Ele é um elemento que criamos para navegar sequencialmente.
# Iterator trabalha com iterável.
# Generator é uma função que pausa.

# O return para a execução da função e retorna o valor. O generator PAUSA a função e isso é muito legal.

# def generator(n=0):
#     yield 1
#     print('step 1')
#     yield 2
#     print('step 2')
#     yield 3 
#     print('finishing')

# gen = generator(n=0)

# while True:

#     try:
#         print(next(gen))
#     except StopIteration:
#         break

def generator(n=0, maximum=5000):
    for number in range(maximum):
        yield number

gen = generator()

for n in gen:
    print(n)