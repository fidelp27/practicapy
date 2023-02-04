'''
collections.deque()

Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

The first line contains an integer N, the number of operations.
The next N lines contains the space separated names of methods and their values.

Output Format

Print the space separated elements of deque d.


Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
'''
from collections import deque
n = int(input())
d = deque()
for _ in range(n):
    func, *args = input().split()
    getattr(d, func)(*map(int, args))

print(*d)
