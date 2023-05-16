'''
Given an array of bird sightings where every element represents a bird type id, determine the id of the most 
frequently sighted type.If more than 1 type has been spotted that maximum amount, returnthe smallest of their ids.

Function Description
Complete the migratoryBirds function in the editor below.

migratoryBirds has the following parameter(s):

int arr[n]: the types of birds sighted

Returns

int: the lowest type id of the most frequently sighted birds
'''

#!/bin/python3

from collections import Counter
#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    bird_count = Counter(arr)
    max_count = max(bird_count.values())
    max_birds = [bird for bird, count in bird_count.items()
                 if count == max_count]
    return min(max_birds)


if __name__ == '__main__':
    arr_count = int(input("cantidad de aves ").strip())
    arr = list(map(int, input("id de las aves ").rstrip().split()))
    result = migratoryBirds(arr)
