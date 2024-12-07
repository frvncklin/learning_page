# Os módulos que importamos seguem o padrão singleton, ou seja
# eles só podem ter uma única instãncia no programa.
# Isso é interessante mas não é bom em todos os casos,
# como em testes unitários.

# Quando importamos um módulo, o Python vai salvar ele
# na memória, e toda vez que o utilizarmos, ele já vai estar
# salvo, não precisando ser importado de novo.
# Eu entendo assim:
# O python ao importar o módulo, o executa dentro do main.
# Ao fazer isso, tudo o que estava e, nosso módulo é salvo 
# e armazenado na memória.
#
# É dessa forma que estou entendendo. 
# Talvez não seja a verdade mas, para mim, faz bastante 
# sentido. Sobretudo em questão de eficiância.

# Pode ser, entretanto, que desejamos recarregar esse módulo
# por algum motivo. Isso é possível.
# basta fazer assim:

import importlib
import importlib.util
import teste1

for number in range(5):
    importlib.reload(teste1)
    # Estou recarrregando o módulo 5 vezes.

# Explorando a bibliotace importlib.

# spec = importlib.util.find_spec('pandas')

# slasher = "\n" + ("-" * (max(len(str(spec.loader)) + len("loader: "), len(str(spec.origin)) + len("origin: "), len(str(spec.name)) + len("name: ")))) + "\n"

# if spec is not None:
#     print("Module found!", slasher, f"\nLoader: {spec.loader}\nOrigin: {spec.origin}\nName: {spec.name}\n", slasher)
# else:
#     raise ModuleNotFoundError("O módulo não foi encontrado")

# O recarregamento de módulos pode ser utilizado quando é 
# feita alguma alteração no outro módulo.
# Ao recarregar, salvamos a versão mais recente daquele módulo
# e, portanto, as alterações feitas.

# Quando saímos do módulo e o executamos de novo, é a mesma 
# coisa que recarregar o módulo.