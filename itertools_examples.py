import itertools
'''
Itertools es un módulo de Python que proporciona funciones
para trabajar con iteradores de forma eficiente. Algunas de las funciones más comunes incluyen:

count(start=0, step=1): devuelve un iterador que genera una serie de números
enteros a partir de un valor inicial y un intervalo de incremento.

cycle(iterable): devuelve un iterador que repite los elementos de un iterable en un ciclo.

repeat(element, times=None): devuelve un iterador que repite un elemento
un número específico de veces, o infinitamente si no se especifica el número de veces.

chain(iterable, ...): devuelve un iterador que concatena los elementos de varios iterables.

zip(iterable, ...): devuelve un iterador que combina los elementos de varios iterables en una tupla.
'''
# Acumulado
accumu = list(itertools.accumulate([1, 2, 3, 4, 5]))
print(accumu)

# chain -> concatena varios iterables
nombre = "Juan"
apellido = "juano"

cha = list(itertools.chain(nombre, apellido))
lista = list(nombre + apellido)
print(lista)
print(cha)

# Count
for i in itertools.count(10, 2):
    print(i)
    if i > 20:
        break


# cycle
colors = ['red', 'green', 'blue']
counter = 5
for color in itertools.cycle(colors):
    counter -= 1
    if counter > 0:
        print(color)
    break

# repeat
for i in itertools.repeat('hello', 3):
    print(i)

# compress  filtra un iterador aplicando una función booleana a sus elementos
print(list(itertools.compress("Fidel", [1, 0, 1, 1, 0])))
for i in itertools.compress("Fidel", [1, 0, 1, 1, 0]):
    print(i)

# output ['F', 'd', 'e']

# dropwhile descarta elementos de un iterador mientras una condición es verdadera.
# Una vez que se encuentra el primer elemento que **no** cumple con la condición,
# se dejan de descartar elementos y se devuelve el resto del iterador.
for i in itertools.dropwhile(lambda x: x < 5, [1, 4, 5, 2, 8, 7]):
    print("dropwhile", i)
    # 5, 2, 8, 7

# filterfalse(): filtra elementos de un iterador que son falsos según una función dada - lo opuesto a la condición
# No para de filtrar
minor_five = list(itertools.filterfalse(lambda x: x > 5, [1, 4, 5, 6, 8, 7]))
print("filterfalse", minor_five)
# [1, 4, 5]

# groupby(): agrupa elementos de un iterador según una función dada

words = ["apple", "banana", "cherry", "apple", "banana", "cherry"]

# Use groupby() to group the words by their first letter
grouped_words = itertools.groupby(words, key=lambda x: x[0])
for letter, group in grouped_words:
    print(letter, list(group))

# islice(): devuelve un iterador que contiene un subconjunto de elementos de otro iterador

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use islice() to get a subiterator with the first 5 elements
# devuelve un iterador que contiene un subconjunto de elementos de otro iterador
sub_iterator = itertools.islice(numbers, 5)
print(list(sub_iterator))
# Output: [1, 2, 3, 4, 5]


# Example for pairwise()
# devuelve parejas consecutivas de elementos de un iterador
numbers = [1, 2, 3, 4, 5]

# Use pairwise() to get consecutive pairs of numbers
pairs = itertools.pairwise(numbers)
print(list(pairs))
# Output: [(1, 2), (2, 3), (3, 4), (4, 5)]

# Example for starmap()
# aplica una función a cada par de elementos de un iterador
# es similar a map() pero trabaja con iteradores que contienen tuplas, es decir,
# en lugar de aplicar una función a cada elemento de un iterador, starmap() aplica una
# función a cada par de elementos de un iterador.
# Es decir, recibe una función y un iterable de tuplas, y aplica la función a cada uno de los elementos de las tuplas.
numbers = [1, 2, 3, 4, 5]

# Use starmap() to square each number
squared_numbers = itertools.starmap(lambda x, y: x*y, zip(numbers, numbers))
print(list(squared_numbers))
# Output: [1, 4, 9, 16, 25]

# takewhile(): devuelve elementos de un iterador mientras una condición es verdadera
# Una vez que se encuentra el primer elemento para el cual la función devuelve falso, takewhile() deja de devolver elementos.
# Example for takewhile()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use takewhile() to get numbers less than 6
less_than_6 = itertools.takewhile(lambda x: x < 6, numbers)
print(list(less_than_6))
# Output: [1, 2, 3, 4, 5]


# tee(): devuelve varios iteradores independientes a partir de uno solo
# Esto significa que puedes consumir uno de los iteradores sin afectar al otro.
# Es útil para tener varias versiones del mismo iterador que se pueden utilizar de forma independiente.
# Example for tee()
numbers = [1, 2, 3, 4, 5]

# Use tee() to create two independent iterators
iterator1, iterator2 = itertools.tee(numbers)

# Consume one of the iterators
print(list(iterator1))
# Output: [1, 2, 3, 4, 5]
# The other iterator is still available
print(list(iterator2))
# Output: [1, 2, 3, 4, 5]

# zip_longest(): combina elementos de varios iteradores en tuplas,
# rellenando con valores predeterminados si alguno se agota antes.
# Example for zip_longest()
numbers1 = [1, 2, 3, 4]
numbers2 = [5, 6, 7]

# Use zip_longest() to combine the lists, filling with None if one is shorter
combined = itertools.zip_longest(numbers1, numbers2)
print(list(combined))
# Output: [(1, 5), (2, 6), (3, 7), (4, None)]
