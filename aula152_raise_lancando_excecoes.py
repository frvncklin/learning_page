# Nós podemos lançar exceções manualmente, e criar nossos
# Próprios erros.
# Desenvolvedores adoram erros e problemas para resolver:
# Não esqueça disso!

# É possível criar um erro, mas para isso precisamos entender
# de classes.

# Vamos lá:

# print(123)
# # raise ValueError('Valor inválido.')  
# # Para executar uma classe, devemos colocar parênteses.
# # Dentro dos Parênteses, digitamos a mensagem de erro.
# print(456)  # Repare como o VSCode já me avisa que não vai
# # ser possível executar o código após o erro.

# # Os erros são utilizados para comunicação principalmente.

# def divide(n, d):
#     if d == 0:
#         raise ZeroDivisionError("Você tentou fazer uma divisão por zero!")
#     else:
#         return n / d
    
# print(divide(9, 0))

# # Dentro de um Ty e Except, eu posso relançar uma exceção ou
# # dar raise em outra exceção.

# # Por exemplo:

# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         # Quando a gente dá raise assim, geralmente é
#         # por que queremos fazer alguma coisa no meio
#         # do erro.
#         # Por exemplo, enviar a informação de que houve erro
#         # para alguma base de dados.
#         raise
#     except TypeError:
#         ...

# # Também é possível usar um try dentro de um try.

# # Precisamos cahamar a função do que ela faz.
# # Se temos uma função que trata erros (o padrão), devemos
# # chamá-la somente para isso.
# # Esta função que temos aqui (divide) apenas faz a divisão
# # Temso que chamar outra função para tratar os erros.

# # Por exemplo:

# def treats_divisions(n, d):

#     while True:
#         try:
#             n / d
#             break
#         except ZeroDivisionError:
#             print("Você tentou dividir por zero.\nPor favor, insira outro número.")
#             d = input(">>> ")
#         except TypeError:
#             print("Você tentou dividir uma string.\nPor favor, insira um número válido.")
#             n = input(f"Corrigindo \'{n}\'\n>>> ") if not isinstance(n, (float, int)) else n
#             d = input(f"Corrigindo \'{d}\'\n>>> ") if not isinstance(d, (float, int)) else d


# def divide(n, d):

#     treats_divisions(n, d)

#     return n / d

# Pode ser feito assim também:

def verify_valid_number(number):

    if isinstance(number, (float, int)):
        return True
    return False

def verify_zero(number):

    if number == 0:
        return True
    return False

def divide(n, d):

    for number in (n, d):
        if verify_zero(number):
            raise ZeroDivisionError("You tried to divide using 0! Be careful.")
        elif not verify_valid_number(number):
            raise TypeError(f"\'{number}\' must be a float or an interger.\nRight now it\'s a [{type(number).__name__}]... change it!")
        else:
            continue
 
    return n / d

        
divide(9.2, "st")

# If it's difficult to name a function, maybe it's better to
# think whether we built that function right.
# Functions must be simple and call upon other functions if 
# necessary.
# Functions must be clear and simple.
# Erros are cool, we'll be launching errors in our program 
# constantly.

