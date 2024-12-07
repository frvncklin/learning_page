import os

from aula186_criando_arquivos_com_python import caminho_arquivo

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo_1:
    arquivo_1.write('Atenção\n')
    arquivo_1.write('Line 2\n')
    arquivo_1.writelines(('Line 3\n', 'Line 4\n'))

# os.remove(caminho_arquivo)  # Isso remove o arquivo do sistema pelo Python.
# Incrível como é possível, com uma linguagem de programação, fazer as coisas que costumamos
# fazer com a nossa interface gráfica do computador.

os.rename(caminho_arquivo, 'arquivo_teste.txt') # Isso renomeia ou move o arquivo.s