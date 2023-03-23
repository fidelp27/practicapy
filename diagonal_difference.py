'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9  

Return

int: the absolute diagonal difference

a = 1 + 5 + 9
b =3 + 5 + 9
abs(a - b)
'''


def diagonalDifference(arr):
    size = len(arr)
    result = 0
    for i in range(0, size):
        result += arr[i][i]
        result -= arr[i][size - 1 - i]
    return abs(result)
