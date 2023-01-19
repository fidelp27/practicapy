import math
import os
import random
import re
import sys


'''
A single line of input containing the full name

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Input: chris alan
Output:Chris Alan
'''
# Complete the solve function below.


def solve(s):
    arr = s.split(' ')
    nuevo = []
    for word in arr:
        print(word[0])
        if word[0].isnumeric():
            nuevo.append(word)
        else:
            nuevo.append(word.capitalize())
    print(" ".join(nuevo))


solve("23fidel parabacuto")
