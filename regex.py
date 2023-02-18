'''
You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5

 Number must contain at least  decimal value.
For example:
✖
 12.
✔
12.0  

 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using float(N).
 
 Input Format

The first line contains an integer , the number of test cases.
The next  line(s) contains a string .
'''

import re
pattern = re.compile(r'^[+-]?\d*\.\d+$')
for _ in range(int(input())):
    print(bool(pattern.match(input())))

#!explicación del código
'''
^ : Ancla que indica el inicio de la cadena.
[+-]? : Corresponde a un signo opcional (+ o -) al comienzo de la cadena. 
\d* : Corresponde a cero o más dígitos. En este caso, representa la parte entera del número decimal.
\. : Escapa el carácter "." para que coincida literalmente con un punto en la cadena.
\d+ : Corresponde a uno o más dígitos después del punto decimal. En este caso, representa la parte decimal del número.
$ : Ancla que indica el final de la cadena.
'''
