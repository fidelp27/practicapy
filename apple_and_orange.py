'''
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. 
Using the information given below, determine the number of apples and oranges that land on Sam's house.

In the diagram below:
* The red region denotes the house, where s is the start point, and t is the endpoint. The apple tree is to the left of
the house, and the orange tree is to its right.
* Assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.
* When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis. *A negative 
value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the 
tree's right. *
'''

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    fall_apples = [x + a for x in apples if x + a in range(s, t+1)]
    fall_oranges = [x + b for x in oranges if x + b in range(s, t+1)]
    print(len(fall_apples), len(fall_oranges), sep="\n")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
