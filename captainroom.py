'''
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K  members per group where K ≠ 1.

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear K times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.

Input Format

The first line consists of an integer, K , the size of each group.
The second line contains the unordered elements of the room number list.

Output Format

Output the Captain's room number.

'''

'''
from collections import Counter
K = int(input())
E = input().split()
rooms = Counter(E)
for i in rooms:
    if (rooms[i] == 1):
        print(i)
        break
'''
#!Esta solución no me la tomó por tiempo de ejecución
'''
K = int(input())
E = input().split()
rooms = {x: E.count(x) for x in E if E.count(x) == 1}
print(*rooms.keys())
'''
