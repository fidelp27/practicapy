'''
Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i < j
and ar[i] + ar[j] is divisible by k.

Example:
ar =[1,2,3,4,5,6]
k=5
Three pairs meet the criteria: [1,4], [2,3] and [4,6].  


Complete the divisibleSumPairs function in the editor below.

divisibleSumPairs has the following parameter(s):

int n: the length of array ar
int ar[n]: an array of integers
int k: the integer divisor

Returns
- int: the number of pairs

Input format:
The first line contains 2 space-separated integers, n and k.
The second line contains n space-separated integers, each a value of ar[i].
'''
from itertools import combinations


def divisibleSumPairs(n, k, ar):
    print(sum(1 for x in combinations(ar, 2) if sum(x) % k == 0))
    return sum(1 for x in combinations(ar, 2) if sum(x) % k == 0)


first_multiple_input = input("Indica los valores de n y k").rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
ar = list(map(int, input("Indica los valores de ar").rstrip().split()))

divisibleSumPairs(n, k, ar)
