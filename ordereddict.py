'''
! An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
If a new entry overwrites an existing entry, the original insertion position is left unchanged.

>>> from collections import OrderedDict
>>>
>>> ordinary_dictionary = {}
>>> ordinary_dictionary['a'] = 1
>>> ordinary_dictionary['b'] = 2
>>> ordinary_dictionary['c'] = 3
>>> ordinary_dictionary['d'] = 4
>>> ordinary_dictionary['e'] = 5
>>>
>>> print ordinary_dictionary
{'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
>>>
>>> ordered_dictionary = OrderedDict()
>>> ordered_dictionary['a'] = 1
>>> ordered_dictionary['b'] = 2
>>> ordered_dictionary['c'] = 3
>>> ordered_dictionary['d'] = 4
>>> ordered_dictionary['e'] = 5
>>>
>>> print ordered_dictionary
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

Task

You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.

item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.

Input Format

The first line contains the number of items, N.
The next N  lines contains the item's name and price, separated by a space.

Print the item_name and net_price in order of its first occurrence.

Input:
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Output
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''
# *Esta clase es una subclase de la clase dict incorporada, pero mantiene el orden de los elementos en el diccionario.
from collections import OrderedDict


# * asigna el valor entero de la entrada dada por el usuario.
cantidad = int(input())
# * crea un diccionario vacío llamado ordered_dict.
ordered_dict = OrderedDict()


# ** La siguiente línea crea un ciclo for que se repetirá el número de veces de cantidad. El _ se usa como un nombre de variable que no se usará en el ciclo.
for _ in range(cantidad):
    # ** La entrada se separa por el argumento maxsplit=1 en las variables item y price.
    # ** La función rsplit() se utiliza para dividir la entrada desde el lado derecho, de modo
    # ** que el último elemento se asigna a price.
    item, price = input().rsplit(maxsplit=1)
    # ** Luego, utiliza el método get() para verificar si el elemento actual ya está en el diccionario ordenado.
    # ** Si es así, agrega el precio al valor existente. Si no, crea una nueva pareja clave-valor con
    # ** el elemento y el precio.
    ordered_dict[item] = ordered_dict.get(item, 0) + int(price)


for item, price in ordered_dict.items():
    print(item, price)
