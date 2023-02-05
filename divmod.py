'''
One of the built-in functions  of Python is divmod, which takes two arguments, a and b, and returns a tuple
containing the quotient of first argument by the second argument and the remainder a.

>>> print divmod(177,10)
(17, 7)

Task
Read in two integers, a and b, and print three lines.
The first line is the integer division a//b (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: a%b.
The third line prints the divmod of a and b.
'''
#!El ejercicio pide las entradas por separado, no en la misma línea
a, b = map(int, input().split())
result = divmod(a, b)
print(*result, result, sep='\n')
