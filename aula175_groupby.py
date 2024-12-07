from itertools import groupby

def order_by_grade(dict):
    return dict['nota']

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

alunos.sort(key=order_by_grade)
# print(alunos)

# alunos_aprovados = [
#     {**aluno}
#     for aluno in alunos
#     if aluno['nota'] not in ('C', 'D')
# ]

# alunos = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c']

groups = groupby(alunos, key=order_by_grade)    # um iterator.

for chave, group in groups:
    group = list(group)
    approved_message = 'Aprovado' if group[0]['nota'] not in ('C', 'D') else 'Reprovado'
    print(f'Grade {chave}: {approved_message}')
    print(group)

# print(alunos_aprovados)

# No groupby, os dados precisam estar ordenados.

# Lembrar sempre que a função gropuby abriga sempre itens consecutivos.