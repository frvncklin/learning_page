def decorator_fabric(param=None):
    def function_fabric(func):
        print('Decorator 1')

        def nested(*args, **kwargs):
            print(f"Decorator codename [{param}]")
            print('Nested')
            result = func(*args, **kwargs)
            return result
        return nested
    return function_fabric

# Agora, tenho acesso a 3 escopos

@decorator_fabric(90281)
def sum(x, y):
    return x + y

# Aqui, o Python vai pegar e tentar executar o blablabla(1,2,3)
# como o blablabla(1, 2, 3) retorna o decorator, ele vai estar
# fazendo isso: decorator() == blablabla(1, 2, 3)()
# Fascinante!

# ten_plus_five = sum(10, 5)
# print(ten_plus_five)

multiply = decorator_fabric(90125)(lambda x, y: x * y)

ten_times_five = multiply(10, 5)
print(ten_times_five)

# No processo em que o decorator 'braça' a nossa função, 
# ela é trocada pela nested.

# Dentro do @, o Python está esperando um decorador e vai 
# tentar executar ele.

# Decoradores com parâmetros nos permitem fazer coisas antes
# mesmo dos decorators!

# As funções decoradores são factory functions: funções que
# criam outras funções ou fábricas de funções.

# Usando a Fábrica de decoradores, eu tenho acesso aos seus 3
# aparãmetros em todos o escopo do decorador como variáveis
# livres, que eu posso usar para configurar ele.