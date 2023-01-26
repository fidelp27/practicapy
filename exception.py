'''
Task

You are given two values a and b.
Perform integer division and print a/b.

Output Format

Print the value of a/b.
In the case of ZeroDivisionError or ValueError, print the error code.
'''
n = int(input())

for i in range(n):

    try:
        a, b = map(int, input().split())
        result = a//b
        print(result)
    except Exception as e:
        print('Error Code:', e, " type:", type(e))
