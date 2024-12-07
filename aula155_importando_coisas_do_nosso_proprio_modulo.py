# Criar módulos propositalmente longe do main pode gerar 
# muitos transtornos.

# O main é o ponto de entrada de nosso programa.

# Quando importamos um módulo, tudo o que está dentro dele
# é executado imediatamente.

from teste1 import system_platform_name_message

print(system_platform_name_message)

# Ou seja, todas as coisas que o outro sistema importou para
# ele se fazem presentes ao importarmos algo do sistema.
# Pois, quando importamos alhguma coisa do sistema, 
# levamos todos os seus imports e executamos ele.
# Dessa forma, todos os comandos imperativos do módulo serão
# inadvertivamente executados, e isso é muito interessante.

# De certa forma, isso garante com que as variáveis do nosso
# módulo possam ser acessadas.