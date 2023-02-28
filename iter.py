'''
Input Format

The input consists of three lines. The first line contains the integer N, denoting the length of the list. 
The next line consists of N space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.

Note: The answer must be correct up to 3 decimal places.

'''
from itertools import combinations
a, b, c = int(input()), input().split(" "), int(input())
comb = list(combinations(b, c))
print(sum([1 for i in comb if "a" in i])/len(list(comb)))
