# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d["A"].append(input())
for i in range(m):
    d["B"].append(input())


for i in range(n):
    d['A'].append(input())
for i in range(m):
    d['B'].append(input())

for i in d['B']:
    if i in d['A']:
        for j in enumerate(d['A'], 1):
            if i == j[1]:
                print(j[0], end=" ")
        print()
    else:
        print(-1)
