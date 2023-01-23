'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
'''
string = "BANANA"


def substring_point(string):
    vocales = ["A", "E", "I", "O", "U"]
    _len = len(string)
    _list = list(string)

    stuart = 0
    kevin = 0

    for i, s in enumerate(_list):
        if s in vocales:
            kevin += _len - i
        else:
            stuart += _len - i

    if stuart > kevin:
        print(f'Stuart {stuart}')
    if stuart < kevin:
        print(f'Kevin {kevin}')
    if stuart == kevin:
        print(f'Draw')


substring_point(string)
