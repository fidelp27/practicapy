'''
Task

You are given a space separated list of integers. If all the integers are positive, 
then you need to check if any integer is a palindromic integer.

The first line contains an integer N. N is the total number of integers in the list.
The second line contains the space separated list of  N integers.

Print True if all the conditions of the problem statement are satisfied. Otherwise, print False.

'''
a, b = input(), input().split()
print(all(int(n) >= 0 for n in b) and any(n == n[::-1] for n in b))

#!condicion elem + for elem in lista
