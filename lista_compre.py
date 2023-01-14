from functools import reduce
# Hacer lista

print(__name__)


def make_list(num1, num2, num3):
    listado = [[a, b, c] for a in range(
        num1+1) for b in range(num2+1) for c in range(num3+1) if (a+b+c) != 4]
    return listado

# Hacer diccionario


def make_dict(number):
    diccionario = {key: key*4 for key in range(number) if key % 2 == 0}
    return diccionario


# Unir listas en diccionario
lista1 = [2, 4, 6, 8]
lista2 = [8, 6, 4, 2]
diccionario2 = dict(zip(lista1, lista2))
print(diccionario2)

# Eliminar repetidos


def delete_repeated(lista):
    lista_sin_repetidos = set(lista)
    print(len(lista_sin_repetidos))
    return lista_sin_repetidos

# Devolver potencia de una lista


def list_pow(lista, exp):
    nueva_lista = map(lambda x: pow(x, exp), lista)
    return list(nueva_lista)


# reduce se importa functools
suma = reduce(lambda a, b: a + b, lista1)
print(suma)

# filtrar valores
filtrada = filter(lambda x: x < 5, lista2)
