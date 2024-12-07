from aula186_criando_arquivos_com_python import caminho_arquivo

# with open(caminho_arquivo, 'w') as arquivo_1:
#     arquivo_1.write('Eu sou um arquivo criado pelo Python!')

# with open(caminho_arquivo, 'r') as arquivo_1:
#     arquivo_1_content = arquivo_1.read()

with open(caminho_arquivo, 'w+') as arquivo_1:
    arquivo_1.write('Eu sou um arquivo criado pelo Python!\n')
    arquivo_1.writelines(('Line 3\n', 'Line 4'))
    # Writelines escreve uma lista de strings no arquivo de uma vez, de uma forma diferente.
    arquivo_1.seek(0, 0)
    arquivo_1_content = arquivo_1.read()
    arquivo_1.seek(0, 0)
    print(arquivo_1.readline(), end='')
    print(arquivo_1.readline().strip()) 
    print(arquivo_1.readline().strip())
    arquivo_1.seek(0, 0)
    print('READLINES')
    for line in arquivo_1.readlines():
        # readlines lê todas as linhas do arquivo de txt e cria uma lista com cada uma delas.
        # Também há o método writelines, que faz a mesma coisa, porêm escrevendo!
        print(line.strip())
    print(type(arquivo_1))
    # O readline está lendo linha por linha.
    # Na estranhe o espaço entre as linhas. Devemos lebrar que o print tem um end que é uma quebra de linha.
    # Ele é muito útil para arquivos grandes que não carregam de uma vez na memória.

# O read() lê o conteúdo completo do arquivo e armazena na 
# variável que escolhemos.
# neste módulo, eu escrevo no arquivo Python e, logo em
# seguida, li seu conteúdo.

# Lembrando que existem vários modos de execução:

print()
print(f"Este é o conteúdo do meu arquivo:\n\n{'-' * len(arquivo_1_content)}\n\n{arquivo_1_content}\n\n{'-' * len(arquivo_1_content)}")

# Lembrar sempre de, após usar o read(), mover o cursor para o topo do arquivo usando seek(0, 0).
# readline() -> Lê o arquivo linha por linha. Caso for printar, atenção ao 'end' da função
# print(). Quando o arquivo termina, o readline() não levanta exceção.
# Para corrigir ess espaço do print, podemos usar o definir o atributo end da função print
# como igual a uma string vazia (end='') ou podemos usar o método (de str) strip(), que elimina os 
# espaços do começo e do fim, incluindo quebras de linha.

"""
   As funções read(), open(), close(), readline(), seek() etc.. São, na verdade, métodos da
   classe TextIOWrapper, que manipula objetos de fluxo que interagem com arquivos de texto. 
"""