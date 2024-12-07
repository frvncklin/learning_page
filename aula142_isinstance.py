sample_list_1 = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {1, 2}, {'nome': 'Victor'}
]

# É muito comum, em nosso mundo da programação, lidarmos com
# listas com múltiplos tipos dentro delas. Entretanto, essa
# é uma má prática.
# Caso coloquemos itens de tipo diferente em uma lista,
# teremos que usar um if lá dentro, e isso fere o liskov 
# substitution principle do SOLID (abordaremos ele mais a
# frente).
def type_detector(sample_list):
    data_quantity = []
    strings_amount = 0
    int_amount = 0
    float_amount = 0
    list_amount = 0
    set_amount = 0
    dict_amount = 0
    bool_amount = 0
    complex_amount = 0

    for item in sample_list:
        if isinstance(item, str):
            strings_amount += 1
        elif isinstance(item, int):
            int_amount += 1
        elif isinstance(item, float):
            float_amount += 1
        elif isinstance(item, list):
            list_amount += 1
        elif isinstance(item, set):
            set_amount += 1
        elif isinstance(item, dict):
            dict_amount += 1
        elif isinstance(item, bool):
            bool_amount += 1
        elif isinstance(item, complex):
            complex_amount += 1

    data_quantity.append(f"Strings: {strings_amount}")
    data_quantity.append(f"Intergers: {int_amount}")
    data_quantity.append(f"Floats: {float_amount}")
    data_quantity.append(f"Lists: {list_amount}")
    data_quantity.append(f"Sets: {set_amount}")
    data_quantity.append(f"Dicts: {dict_amount}")
    data_quantity.append(f"Boolean: {dict_amount}")
    data_quantity.append(f"Complex: {dict_amount}")
    
    print(f"Types of Data in {__name__}:")
    print(*data_quantity, sep='\n')

type_detector(sample_list_1)

# Como tipos diferentes possuem métodos diferentes, isso pode 
# Quebrar o programa.
# o VsCode é muito inteligente. Ele fica, o tempo todo, 
# Rodando um server que verifica o nosso código.
# Isso é algo bem complexo, que nós não temos total noção.

# Ao passarmos mais de um tipo no isinstance(), isso equivale
# a um "ou".

# O isinstance será nosso companheiro constante quando formos
# Trabalhar com os tipos que não são uniformes.
# Não são boas práticas, mas acontece, principalmente em 
# dicionários.