'''
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'. The first substring is all 'A'
characters, so u1=A. The second substring has all distinct characters, so u2 = BCA .
The third substring has 2 different characters, so u3 = DE. Note that a subsequence
maintains the original order of characters encountered. The order of characters in each
subsequence shown is important.

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze

Prints

Print each subsequence on a new line. There will be n/k  of them. No return value is expected.

Input Format

The first line contains a single string, s.
The second line contains an integer, k, the length of each substring.

Input
STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Output
AB
CA
AD
'''
import textwrap
word = input("Escribe la palabra")
agrupador = int(input("Escribe la cantidad de letras por grupo"))
lista = textwrap.wrap(word, agrupador)
for word in lista:
    print(''.join(list(dict.fromkeys(word))))


'''
La función "dict.fromkeys(word)" elimina
los duplicados de la lista "word", ya que un diccionario solo puede tener claves únicas.

{'A': None, 'B': None}
{'C': None, 'A': None}
{'A': None, 'D': None}

La función "list()" convierte el diccionario resultante en una lista.
Esto es útil porque los diccionarios no son ordenados y las listas son.

['A', 'B']
['C', 'A']
['A', 'D']

La función "join()" se utiliza para unir todos los elementos de una lista en una cadena,
utilizando el separador especificado (en este caso, una cadena vacía "''").

AB
CA
AD
'''
