'''
itertools.combinations(iterable, r)
This tool returns the r length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sorted order.
So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Task

You are given a string S.
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
'''
from itertools import combinations

S, K = input().split()
result = []

for i in range(1, int(K)+1):
    comb = ["".join(i) for i in list(combinations(sorted(S), i))]
    result.extend(comb)

# ** El asterisco (*) antes de la variable "result" en
# * la línea de impresión es un operador de desempaquetado (unpacking operator) en Python.
print(*result, sep="\n")
