'''
Task
You have a non-empty set s, and you have to execute N commands given in N lines. The command will be pop, remove and discard.

Input Format

The first line contains integer n, the number of elements in the set s.
The second line contains n space separated elements of set s. All of the elements are non-negative integers,
less than or equal to 9.
The third line contains integer N, the number of commands.
The next line contains either pop, remove or discard commands  followed by their associated value.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop
discard 6
remove 5
pop
discard 5
Sample Output

4
'''

'''
func, *args = input("Dame el método y argumentos").split()
getattr(lst, func)(*map(int, args))
'''

n = int(input("cantidad de caracteres"))
s = set(map(int, input("caracteres separados por espacios").split()))
for _ in range(int(input("cantidad de comandos"))):
    try:
        *args, func, q = input("comando + numero separado por espacios").rsplit(2)
        if func != "pop":
            getattr(s, func)(*list(map(int, args)))
        else:
            s.pop()
    except Exception as e:
        print(e)
print(sum(s))
