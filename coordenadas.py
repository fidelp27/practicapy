# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_cartesian_plane(A, B):
    lista = [(i, j) for i in A for j in B]
    print(lista)
    return lista


get_cartesian_plane([1, 2], [3, 4])
