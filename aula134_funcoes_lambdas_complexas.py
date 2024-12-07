def execute(func, *args):
    return func(*args)

def create_multiplier(multiplicator):
    def multiply(number):
        return number * multiplicator
    return multiply

times_two = create_multiplier(2)

print(times_two(200))
print(times_two(800))

# As the create multiplier function returns the multiply function. We can use this to crate an instance of the
# multiply function easily.

# This could be done like this:

# func = lambda parameter: parameter
# But this is a bad practice. The PEP 8 doesn't recommend we do it!

# print(
#     execute(
#         lambda x, y: x + y, 2, 3
#     ),
#     execute(sum(2, 3))
# )

# A estrutura do lambda é essa aqui: lambda argumentos: retorno da função, argumentos.

# Geralmente estruturas lambdas são utilizadas por usa legibilidade. Não são feitas muitas funções lambdas 
# complexas.

# Fazendo o equivalente da nossa função multiplica, temos:

duplicate = execute(
    lambda m: lambda n: n * m, 2
)

# Se a leitura do código está complexa, então tem algo estranho no código.
# Pode ser que estejam faltando variáveis: Variáveis são utilizadas para deixar o código mais legível.

# Por último, podemos passar args também.

print(
    execute(
        lambda *args: sum(args),
        1, 2, 3, 4, 5
    )
)

# Existe uma função sum. Estamos passando para ela vários args de uma vez e executando-a utilizando a função
# execute.