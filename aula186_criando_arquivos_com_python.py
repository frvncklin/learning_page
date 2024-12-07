# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = r'C:\Users\victo\Desktop\Learning\Python\arquivo_aula186.txt'
print(caminho_arquivo)
# O caminho, em Pyhton, é sempre relativo a onde eu estou!
# O python tem muita dificuldade em entender essa '\', 
# pois é um caractere de escape.

# Vamos abrir um arquivo criando ele:

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# r - read, w - write, x - Create, a = write in end,
# b - binary, t - modo texto, + (leitura e escrita)

# Sempre fechar o arquivo ao fechar. Sempre incluir essa
# função em um finally.

# Context Manager - with

# O python utilizar o duck typying, onde ele infere os tipos das variáveis.
# quando abrimos e fechamos um arquivo, o Python já insere aquele objeto na classse context manager.
# da mesma forma que, quando criamos um objeto com __iter__ e __next__, estamo criando um iterator.

# Quando escrevemos with_open, o Python já vai abrir e fechar o arquivo, não importa o que ocorra.

# with open(caminho_arquivo, 'w') as arquivo:
    # Quando eu declaro with open eu garanto que o arquivo
    # vai ser aberto e fechado da melhor forma possível.

