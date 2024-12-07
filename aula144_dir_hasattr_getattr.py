# É uma coisa muito corriqueira. Usamos para checar coisas dentro de um determinado objeto.

def reverse_str(str, capitalize):
    new_str = ''
    for str_index in range(-1, -(len(str) + 1), -1):
        new_str += str[str_index]
    if capitalize:
        new_str = new_str.capitalize()  
    return new_str

text = "My Name is Victor"
print(reverse_str(text, True))

# O dir mostra todos os atributos e métodos definidos no objeto. Atributos são nomes que estão definidos.

# Métodos são ações.

# hasattr - checa se tem determinado método.
# getattr - pega o método.

# os nomes dos métodos sempre são strings.

if hasattr(text, 'upper'):
    print('yes')
    print(text.upper())
    # Ou:
    print(getattr(text, 'upper')())

method = 'lower'
print(getattr(text, method)) # ---> Aponta pro método.
print(getattr(text, method)()) # Todo método é executável quando colocamos os '()'. Executa o método.
