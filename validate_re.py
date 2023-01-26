'''
Validar RE de un input

input:
2
.*\+
.*+

output:
True
False
'''

import re

n = int(input())
for i in range(n):
    exp = input()
    try:
        re.compile(exp)
        print('True')
    except:
        print('False')
