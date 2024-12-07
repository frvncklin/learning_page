# Count é um iterator sem fim.

from itertools import count

c1 = count(start=8, step=8)
# Lembrar sempre que o count é um iterator infinto!
r1 = range(8, 100, 8)

print('c1', hasattr(c1, '__iter__'))
# Se tem o método iter, é um iterável.
print('c1', hasattr(c1, '__next__'))
# Se é um iterável e tem um next, então é um iterator.

# Já o range é um oiterável, mas não é um iterator.

print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

# Quando a gente chama um iter o iterator, ele nos retorna 
# ele mesmo.
# for i in range(10):
#     print(next(c1))
    # O next nos entrega o valor e, então, soma mais 1.

print('count')
for i in c1:
    if i > 100:
        break
    print(i)

print()

print('range')

for i in r1:
    if i > 100:
        break
    print(i)

# A grande diferença é que o range tem um fim e o range
# não é um iterator.