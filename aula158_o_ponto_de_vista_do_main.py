# O ponto de vista do main pode te confundir em alguns casos.

# O ponto de vista do main é o path que estamos lidando.

# Por padrão, o sys.path do Python já possui alguns caminhos 
# Definidos pois, como dito antes, ele já vem "com pilhas"
# Mas nós podemos, em nosso main modificá-lo à vontade.

# Tudo que importamos para um módulo, o Python permite sua 
# exportação.

# MAS temos sempre que lembrar que IMPORTAR um módulo 
# significa executar ele e salçvar na memória como se ele
# estivesse dentro do main.
# Ou seja, temos que tomar cuidado com o ponto de vista.
# Caso um módulo faça importações, talvez elas não funcionem
# em um main caso ele seja importado por esse main, devido
# ao problema do ponto de vista.

# TODAS AS IMPORTAÇÕES DO PROGRAMA INTEIRO TEM QUE SER 
# RELATIVAS AO MAIN.

# Por conta disso pode acontecer de alguns módulos não 
# conseguirem ser executados diretamente, devido ao ponto de
# vista estar relacionado ao main.

# Lembrar que, em programação, o "." significa "a pasta em "
# que estou.

import useful_funcs

# O __init__ permite que seja mostrada uma mensagem assim que 
# nós importemos uma pasta.
# Mas não só isso: ele também permite que nós façamos a
# importação dos módulos ao importar o package.
# Provavelmente as grandes bibliotecas do Python funcionam com
# base nessa funcinalidade do init.
# Isso faz com que o package passe a se comportar como um 
# módulo, algo que nosso professor Luiz Otávio Miranda chama,
# carimnhosamente de 'enganar o python'.

# Inclusive, dessa forma somos capazes de fazer from import
# diretamente do Package, pois o Python vai considerar o 
# package como um módulo,