'''
Task
Given an integer,n , and n space-separated integers as input, create a tuple,t , of those n integers.
Then compute and print the result of hast(t).

The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n  space-separated integers describing the elements in tuple t.

Output format:
Print the result of hash(t).

sample input:
0
1 2

sample output:
3713081631934410656
'''

if __name__ == '__main__':
    n = int(input("Cuantos numeros"))
    integer_list = map(int, input("Escribe el numero").split())
    print(tuple(integer_list))
    cripto = hash(tuple(integer_list))
    print(cripto)
