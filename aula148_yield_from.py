# Yield from

def gen1():
    yield 1
    yield 2
    yield 3
    
def gen2():
    yield 4
    yield 5
    yield 6

# Como o generator pausa, ele é perfeito para executar códigos em ordem.

def gen3():
    yield from gen1()
    yield from gen2()

gen_sample = gen3()
for number in gen_sample:
    print(number)

# Dá pra puxar os yields de outro generator usando o comando 'yield from'. Isso é uma ferramenta bem legal.
# Com isso, dá pra linkar vários generators em uma função só.
# Você basicamente chama um generator dentro de outro generator.

# Você pode pasar um generator como argumento para uma função e executar ele dentro dela.

# Outra coisa legal de lembrar: Parâmetros padrão.

