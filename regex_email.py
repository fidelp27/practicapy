'''
You are given an integer N followed by N email addresses. Your task is to print a list
containing only valid email addresses in lexicographical order.
Valid email addresses must follow these rules:
It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores 
The website name can only have letters and digits 
The extension can only contain letters 
The maximum length of the extension is 3. 
'''

#!La letra "r" antes de la comilla simple o doble que delimita el patrón
#! de expresión regular indica que se trata de una "cadena de texto en bruto" o "raw string" en inglés.

# **Esto significa que los caracteres de la cadena, incluyendo los
# **caracteres de escape como \n o \t, se interpretan literalmente y no se tratan como caracteres especiales.
import re


def fun(s):
    return re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', s)
