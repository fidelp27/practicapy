'''
? itertools.combinations_with_replacement(iterable, r)
This tool returns  length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.

Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

Task

You are given a string S.
Your task is to print all possible size K  replacement combinations of the string in lexicographic sorted order.

Sample Input

HACK 2
Sample Output

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''
from itertools import combinations_with_replacement
S, K = input().split()

lista = []
print(*["".join(i)
      for i in (list(combinations_with_replacement(sorted(S), int(K))))], sep='\n')
