# Try, except, else e finally

# try:
#     a = 18 / 0
#     print(a)
# except ZeroDivisionError as error:
#     print("Você tentou dividir por zero!\n-> Nome da Classe Exceção:", f"{error.__class__.__name__}\n-> Texto da Exceção: {error}")

# A meu ver, o try except é uma excelente ferramenta.

# Erros não devem passar silenciosamente, a não ser que explicitamete silenciados (The Zen of Python).

# A partir do momento que o try detecta algum erro de qualquer natureza (que não seja de sintaxe), 
# ele pula direto para o except.

# Em Python, exceções são classes.

# Temos uma classe mãe, Exception, e todas as outras classes herdam dela.
# Classes, no Python, são representadas em PascalCase.

# A finalidade do Try Except é TRATAR ERROS. Lembrar disso.

# quando eu faço except ZeroDivisionError as error
# Eu estu salvando a instância do erro (objeto de erro)
# na variável erro.

# string = 'Luiz' # Isso é uma instância da classe str.
# print(isinstance(string, str))  # Retorna True.

# Geralmente, pra gente, vai ser interessante mesmo exibir só 
# a mensagem de erro (instância do objeto) por que
# O usuário final não vai saber do que se trata aquela classe.
# Entretanto, também pode ser que deixemops isso em algum 
# arquivo, algum log etc.

try:
    print('OPEN FILE')
    print(1)
    a = 8 /0
except ZeroDivisionError as error:
    print("Você tentou dividir por zero!", f"-> Nome da Classe da Exceção: {error.__class__.__name__}", f"-> Texto da Exceção: {error}", sep='\n')
finally:
    # Este bloco sempre será executado.
    # Podemos ter um try sem except, mas precisa de pelo menos
    # um finally.
    # Lembrar sempre do Zen of Python.
    print(2)
    print('CLOSE FILE')
    # Graças ao Finally, conseguimos, de todo jeito, 
    # abrir e fechar o arquivo de forma segura e legível
    ...

# Por exemplo: usamos um finally para abrir um arquivo e
# queremos, ao final, fechá-lo de qualquer forma, independente
# do que acontece. Nesse sentido, o finally é uma ferramenta
# Muito interessante! Pois nos permite fazer uma ação inde-
# pendente dos erros ocorridos durante o try e except.
# Isso torna o código ainda mais legível.

# O finally é geralmente utilizado para fechar arquivos ou
# liberar recursos. É muito útil pois nos dá segurança
# independente de ocorrer uma exceção ou não, sem que nós
# tenhamos que inserir esse comando em todos os Excepts.

# O uso de else no try, except e finally nõa é comum.

# O else é executado caso o código ocorra sem erros,
# o que também é válido.

# Um exemplo:

try:
    print('Open file')
    b = 9 / 0
except ZeroDivisionError as error:
    print("Erro detectado!", f"\n-> Nome: {error.__class__.__name__}\n-> Mensagem: {error}")
    print('Tratar exceção')
else:
    print('Não ocorreu erro!')
finally:
    print('Fechar arquivo')