'''
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print

The four values must be printed on a single line in the order specified above for each i  from l  to number. Each value should 
be space-padded to match the width of the binary value of number  and the values should be separated by a single space.

Sample: 
Input: 17

Output:
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
'''

'''
La línea "pad = number.bit_length()" está obteniendo la longitud 
en bits del número dado. Esto es útil para determinar cuántos dígitos hay en un número en su representación binaria. 
'''


def print_formatted(number):
    for i in range(1, number+1):
        pad = number.bit_length()
        decimal = str(i).rjust(pad)
        octal = str("{:o}".format(i)).rjust(pad)
        hexadecimal = str(format(i, "X")).rjust(pad)
        binario = str(format(i, "b")).rjust(pad)
        print(f'{decimal} {octal} {hexadecimal} {binario}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
