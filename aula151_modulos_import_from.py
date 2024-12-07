# O python vem "com pilhas":
# Ele vem com muitos módulos por padrão.

# Importing a whole module does not change anything in our
# program.
# But we must remember that importing asterisks (*) is a
# bad practice.

import sys
# the same as:
# from sys import exit, platform

# but, if I create a variable with the same names as the above
# it'll change their name, so it's dangerous.
# Be careful.
# Importing a whole module.
# We can also import a part of it

# print("1, 2, 3, exitting...")
# print("System Platform:", sys.platform)
# sys.exit()  # This function exits our program.

# When we import an entire module me must use it's namespace 
# to call their methods.
# I believe this is done for security and legibility.
# Just confirmed that this protects the module's variables
# from coinciding with the ones on the main.

# As variáveis apontam para endereços na memória.
# Se colocarmos um novo ponteiro para a variável, perdemos
# o que ela estava apontando antes.

import sys
# O path são lugares onde o Python vai procurar módulos
# ao iniciar.
# Podemos adicionar um novo caminho a esse path usando o
# sys.path.append('caminho do módulo')

# Um exemplo:

try:
    sys.path.append('/home/hello')
except ModuleNotFoundError as error:
    print("O módulo não foi encontrado!", "\nNome do erro:", error.__class__.__name, "\nDescrição do erro:", error)

print(*sys.path, sep='\n')

# A não ser que trabalhemos com sistemas legados, é bem mais
# comum criarmos os módulos do sistema em volta do main.
# Dessa forma, criando sempre arquivos "para dentro".