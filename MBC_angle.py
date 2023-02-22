'''
ABC is a right triangle, 90°  at B.
Therefore, ABC = 90°.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find  MBC (angle , as shown in the figure) in degrees.

The first line contains the length of side AB.
The second line contains the length of side BC.
Output MBC in degrees.

Note: Round the angle to the nearest integer.
'''

from math import atan, degrees
AB = int(input())
BC = int(input())

angleC = atan(AB/BC)
print((round(degrees(angleC))), chr(176), sep='')
