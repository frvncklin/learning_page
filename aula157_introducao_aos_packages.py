# Podemos ter pastas também, que são chamadas de package 
# em Python.
# Packages são pastas que contêm módulos Python.

# Uma excelemnte forma de lidar com eles é criar um arquivo
# de entrada, um main e criar pastas com módulos de 
# funções e caracerísticas semelhantes que vão ser importados
# ao main, que fará a execução.

# Lembrar do termo "Proteção de namespace".

from useful_funcs.type_detector import type_detector


sample_list = [0, 22.8, "Olá mundo"]
type_detector(sample_list)

# Criar uma função que não retorna nada é como criar um método
# void em Java.

# O main é o arquivo de entrada para o qual vamos importar os
# Outros módulos.

# Podemos controlar o '*' (all) da pessoa usando __all__ =
# [ 'aqui dentro colocamos tudo o que quermos que vá no "*"' ]
# Isso nos dá um bom controle sobre a importação do '*'.

