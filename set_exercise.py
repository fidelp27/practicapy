'''
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. 
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers

float: the resulting float value rounded to 3 places after the decimal

The first line contains the integer,N , the size of arr.
The second line contains the N  space-separated integers, arr[i].
'''
from statistics import mean


def average(array):
    # your code goes here
    no_repeated = set(array)
    avg = mean(no_repeated)
    print(round(avg, 3))


average([1, 2, 3, 4, 5, 6, 2, 4, 5, 6, 8])
