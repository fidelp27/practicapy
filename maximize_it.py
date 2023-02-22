

K, M = map(int, input().split())
lst = []
for _ in range(K):
    N = map(int, input().split())
    lst.append(max(N))
print(lst)
print(sum([x*x for x in lst]))
