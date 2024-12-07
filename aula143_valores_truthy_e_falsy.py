lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None     # None não possui um inverso.
falso = False
intervalo = range(0)
# Todos estes valores são considerados Falsy.
# Outros valores que fujam dessa regra serão truthy.
# Alguns valores, em Python, são considerados falsy.
# Isso significa que, se fizermos um If com esses valores,
# Eles serão considerados falsos.

# Tipos Mutáveis: [] set() {}
# Imutáveis: () "" 0 0.0 None False range(0, 10)

# Os tipos imutáveis só podem ser alterados pela reatribuição.

def truthy_or_falsy(value):
    return 'falsy' if not value else 'truthy'

print(truthy_or_falsy(lista))
print(truthy_or_falsy(dicionario))
print(truthy_or_falsy(conjunto))
print(truthy_or_falsy(tupla))
print(truthy_or_falsy(string))
print(truthy_or_falsy(inteiro))
print(truthy_or_falsy(flutuante))
print(truthy_or_falsy(nada))
print(truthy_or_falsy(falso))
print(truthy_or_falsy(intervalo))

# Ou seja, falsy é um valor que não é um boolean mas é considerado False.