# Existem linguagens mais voltadas para programação funcional (como Golang), portanto é mais comum nessas 
# Linguagens o uso de recursividade.
# Entretanto, a recursividade também é usada com certa frequência fora desse contexto. 

# Lembrando que a call stack tem um limite de cerca de 1000 chamadas. E, além das funções, nela tem o módulo
# a primeira execução...

# Ainda assim, é possível configurar um limite de recursão usando;
# import sys
# sys.setrecursionlimit()

# De qualquer forma, é importante lembrar que, ao executar uma função, seu espoco inteiro fica salvo na 
# memória, então cabe aqui a sensatez.

def factorial(number, number_factorial=1):

    if number <= 1:
        return number_factorial
    
    number_factorial *= number
    number -= 1
    return factorial(number, number_factorial)

print(factorial(10))

# Até umas 500 recursões, estamos seguros, agora, chegando em 1000, já temos um problema.