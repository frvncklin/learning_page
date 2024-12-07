# Decorators: Coisas que decoram outras coisas.
# Há um padrão de projeto para decorators.
# O python criou seu próprio decorator.

# Recebe algo, decora algo, retornando algo ou não.

# Decorar: Adicionar, Remover, Re*stringir ou Alterar funções.

# Decoradores usam clojures.

def is_string(param):
    if isinstance(param, str):
        return True
    return False

def transforms_into_string(value):
    value = str(value)
    return value

def string_validator(func):
    def wrapper(*args, **kwargs):
        # Pre-function treatment.
        for arg in args:
            arg = transforms_into_string(arg) if not is_string else arg
        # Executing function
        result = func(*args, **kwargs)
        # Returning executed function
        return result
    return wrapper

@string_validator
def inverts_string(string):
    # O python troca a nossa função pelo wrapper.
    return string[::-1]

# Isso seria o mesmo se fiséssemos isso: 
# string_validador(inverte_string(string))

# Quando colocamos o '@' do decorator em cima da função, o
# Python passa a executar ela dentro do decoradort


inverted_string = inverts_string("victor francklin miranda")

print(inverted_string)

# Basicmante os decoradores são uma forma elegante e simples
# De fazer alterações em uma função.


