# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

# Recurividade: Algo que se chama de volta. é uyma função que retorna ela mesma.
# Isso gera um loop, como se fosse um for ou While.

# Elas podem ser usadas para dividir um problema grande em partes menores.
# Entretanto, isso funciona melhor para problemas uniformes.
# Caso seja um problema heterogênio, teremos que fazer vários IFs e carregar o estado para a próxima
# execução da função.

# Geralmente é possível transformar laços em funções recursivas.

def recursiva(start, end):
    # Caso recursivo: Contar até chegar até o final.
    if start == end:
        return start
    
    start += 1
    print(start)



    return recursiva(start, end)

print(recursiva(0, 20))

# O único problema é que quando retornamos a função de novo, nós criamos uma nova stack.
# As stacks ocupam memória, pois o escopo da função vai para a memória.

# Toda recursão precisa de um caso base, ou seja, um caso que para a recursão, por motivos óbvios de 
# segurança.

# Sempre que uma função é executada, o escopo dela fica na memória para que as suas variáveis sejam lembradas
# Quando usamos a recursividade, chamamos diversas ocorrências de funções e, com isso, diversos escopos
# ficam guardados. O mesmo ocorre também em closures, onde o Python fica com aquele escopo guardado na
# memória até que ele seja finalizado.

# Entretanto, o Python é eficiente na geração de escopos, portanto, as vezes ainda que seja gasto um pouco
# mais de memória, ainda é válido usar a recursividade, principalmente em casos nos quais o código fica
# mais legível e flexível.