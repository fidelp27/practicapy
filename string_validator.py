'''
Python has built-in string validation methods for basic data. 
It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

Task 
You are given a string. Your task is to find out if the string  contains: alphanumeric characters, 
alphabetical characters, digits, lowercase and uppercase characters.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

La función any() toma un iterable como argumento 
y retorna True si por lo menos uno de los elementos del iterable es True
'''

if __name__ == '__main__':
    s = input()
    n = len(s)
    print(any(s[i].isalnum() for i in range(n)))
    print(any(s[i].isalpha() for i in range(n)))
    print(any(s[i].isdigit() for i in range(n)))
    print(any(s[i].islower() for i in range(n)))
    print(any(s[i].isupper() for i in range(n)))
