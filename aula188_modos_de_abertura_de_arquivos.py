"""
    r -> Modo de leitura, ele lê um arquivo que já existe, mas não cria um.
    w -> Cria um arquivo novo ou sobrescreve o arquivo presente no caminho informado.
    + -> Adiciona possibilidade de escrita no R e leitura no W.
"""

from aula186_criando_arquivos_com_python import caminho_arquivo

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo_1:
    # O modo 'w' apaga tudo o que está no arquivo e escreve de novo.
    arquivo_1.write('Atenção\n')
    arquivo_1.write('Line 2\n')
    arquivo_1.writelines(('Line 3\n', 'Line 4\n'))
# with open(caminho_arquivo, 'a') as arquivo_1:
#     arquivo_1.write('Line 5\n')
#     arquivo_1.write('Line 6\n')

# O 'a' não é muito diferente do 'w', porém ele adiciona algo ao final do arquivo. Ele se
# Chama 'append mode'.

# Já o 'b' abre o arquivo em modo binário, op que não nos permite fazer muitas coisas com ele.
# Vamos retornar a ela mais pra frente no curso.

# Há algo chamado encoding. Cuidado ao usar acentos, caracteres especiais incomuns e afins, pois
# a tabela de conversão que está sendo utilizada pode não ser a UTF-8.
# Sistemas baseados em UNIX, como o Linux e o Mac não costumam ter esses problemas, pois eles
# Utilizam o sistema de codificação de caracteres UTF-8, que é a mesma que vem por padrão
# no VSCode. No Windows, é o Windows 1252.
# Portanto, lembre-se sempre do encoding do arquivo!