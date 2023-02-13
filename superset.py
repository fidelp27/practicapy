'''
You are given a set A and n other sets
Your job is to find wheter set A is strict superset of each of the N sets.
Print True, if A is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.


Input Format

The first line contains the space separated elements of set A.
The second line contains integer n, the number of other sets.
The next n lines contains the space separated elements of the other sets.
'''

A = set(map(int, input().split()))
b = int(input())
flag = []
for _ in range(b):
    _ = set(map(int, input().split()))
    if not A.issuperset(_):
        flag.append(False)
if False in flag:
    print(False)
else:
    print(True)
