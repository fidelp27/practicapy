'''
You are given two sets,A  and B.
Your job is to find whether set A  is a subset of set B.

if set A is subset of set B, print True.
If set A  is not a subset of set B, print False.

Input Format

The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.
'''

for _ in range(int(input())):
    input()
    a = set(map(int, input().split()))
    input()
    b = set(map(int, input().split()))
    print(a.issubset(b))
