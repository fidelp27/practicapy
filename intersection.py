'''
Input Format

The first line contains , the number of students who have subscribed to the English newspaper.
The second line contains  space separated roll numbers of those students.
The third line contains , the number of students who have subscribed to the French newspaper.
The fourth line contains  space separated roll numbers of those students.

Output Format

Output the total number of students who have subscriptions to both English and French newspapers.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output

5
'''

a, *n = map(int, input().split())
z, *b = map(int, input().split())

inter = set(n) & set(b)
print(len(inter))
