'''
Let's learn about list comprehensions! You are given three integers  and  
representing the dimensions of a cuboid along with an integer . Print a list of all
possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal 
to n. Here, 0<=i<=x;0<=j<=y;0<=k<=z Please use list comprehensions rather than multiple 
loops, as a learning exercise.
'''
x = 1
y = 1
z = 2
n = 3
lista = [(i, j, k) for i in range(x+1)
         for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
print(lista)
