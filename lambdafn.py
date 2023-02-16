'''
Let's learn some new Python concepts! You have to generate a list of the first N fibonacci numbers, 0  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Concept

The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables.
Let's say you are given a list of names, and you have to print a list that contains the length of each name.

Note:

Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries.

Input Format

One line of input: an integer N.

Output Format

A list on a single line containing the cubes of the first  fibonacci numbers.

Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
'''


def cube(x): return x**3


def fibonacci(n):
    # return a list of fibonacci numbers
    lst = []
    for i in range(n):
        if (i < 2):
            lst.append(i)
        else:
            lst.append(lst[i-1] + lst[i-2])
    return lst


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
