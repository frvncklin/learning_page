# O iterável detem os valores.
# O iterator entrega um valor por vez.

# O iterator não tem índice ou len.

# A única coisa que o iterator sabe é o next.

# Nosso curso terá uma seção inteira destina aos design pattenrs.

# O iterator não conhece nada do iterável além do seu próximo valor.
# O Python utiliza ducktyping.

iterable = ['I', 'have', '__iter__']    # tem __iter__
iterator = iter(iterable)   # tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))
# Quando o iterator já iterou sobre todos os valores, ele levanta uma exceção de StopIteration.
# O nosso for já sabe quando parar nesse caso, antes que a exceção ocorra.

# O for funciona mais ou menos assim:

def the_for(iterable):
    iterator = iter(iterable)
    try:
        next(iterator)
    except StopIteration:
        exit()
# é mais ou menos isso que ele faz, rudimentarmente.

