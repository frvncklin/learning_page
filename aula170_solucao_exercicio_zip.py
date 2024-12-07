from exercises.ex5_unite_lists import list_cities, list_states
from itertools import zip_longest
print(list(zip(list_cities, list_states)))
print(list(zip_longest(list_cities, list_states, fillvalue='NO CITY')))
