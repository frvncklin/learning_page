"""
O JSON é uma estrutura de dados criada para que nós transportemos ou salvemos dados.
É uma estrutura de dados super simples. Contanto que eles estejam no formato correto,
podem haver diferentes tipos de dados nele (5 no total) Ex: boolean, number, null, string,
array, objeto...

Vai ser similar ao objeto do JS, e ao dicionário do Python (principalmente).
JSON -> Javascript Object Notation.

Arquivos JSON precisam ter a extensão .json.

É muito comum receber de uma API um JSON com um pacote de valores, uma array com várias coisas, ou
um JSON com um objeto dentro dele.
Por exemplo, quando buscamos um usuário na API, o que vai ser retornado para nós é um objeto.
Nesse caso, retornaria algo assim:
[
    {
    "name": "Victor", 
    "lastName": "Francklin", 
    "age": 26,
    "adresses": [ {"line1": "Rua Delhi 137"}, {"line2": "Rua Deocleciano Ramos 740"},] 
    },
    {
    "name": "Gabrielle", 
    "lastName": "Souto", 
    "age": 25 
    },
    {
    "name": "Gabriel", 
    "lastName": "Francklin", 
    "age": 24 
    }
]
chave: valor
Por obrigatoriedade, as chaves precisam ter aspas duplas.

O JSON é muito utilizado para recebermos respostas.
"""
import json
import os

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Francklin',
    'enderecos': [
        {'rua': 'Delhi', 'logradouro': 137, 'complemento': 'FUNDOS'},
        {'rua': 'Deocleciano Ramos', 'logradouro': 740, 'complemento': 'LOTE 2'}
    ]
}

BASE_DIR = os.path.dirname(__file__)    # Retorna o diretório deste arquivo.
SAVE_TO = os.path.join(BASE_DIR, 'arquivo_python.json') # Concatena o diretório de BASE_DIR com
# O nome e a extensão do nosso arquivo, que vamos criar aqui no Python.
# Basicamente aqui ele montou o caminho do diretório usando os.path. Primeiro capturando o
# nome do diretório desse arquivo aqui e depois concatenando ele com o nome desejado do nosso
# arquivo. Criando assim, com sucesso, o diretório de nosso novo arquivo nessa mesma pasta.
# Incrível!
name, extension = os.path.splitext(SAVE_TO)
is_json = extension == '.json'

# Criando o arquivo.
with open(SAVE_TO, 'w') as arquivo:
    json.dump(pessoa, arquivo, indent=2)


print(is_json)

# Existem json.dump() e json.dumps().
# O json.dump() converte um objeto Python em uma string JSON e grava essa string em um arquivo.
# o json.dumps() converte um objeto python em uma String e JSON e RETORNA essa string.

# Também há o json.load() no qual nós carregamos o JSON, que está em um arquivo, em uma variável.

with open(SAVE_TO, 'r') as arquivo:
    pessoas_backup = json.load(arquivo)

print(type(pessoas_backup))

print(json.dumps(pessoas_backup))   # Aqui, estou fazendo o processo inverso. Estou convertendo
# O JSON que estava no aquivo.json da minha pasta e foi transferido para a variável com o load
# de volta em string e jogando ele no meu print.
# O conteúdo que o dumps 'cospe' é uma string e não um dicionário!

# dump -> joga / load -> carrega de volta.

# vamos fazer uma brincadeira:

pessoas_string = json.dumps(pessoas_backup)
pessoa_backup_2 = json.loads(pessoas_string)    # O loads carrega aquela string JSON em uma 
# variável de novo, já convertendo ela para um dicionário.
print(type(pessoa_backup_2))

# procure sempre ler dumps como 'converter json em string e cuspir' e loads como 
# converter uma string que era um json em json de novo e carregar em algo.

# Já o dump é 'carregar um json diretamente em um arquivo'
# e o load é 'pegar um json de um arquivo e devolver ele para uma variável'

# Um json, no Python, é equivalente ao tipo 'dict' e há uma conversão implícita acontecendo a
# todo momento quando usamos os métodos da biblioteca json.

"""
Geralmente, JSONs são utilizados em respostas de APIs ou em arquivos de configuração (como no
próprio VSCODE).
"""