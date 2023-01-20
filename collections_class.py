'''

collections.Counter()
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N  number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu  earned.
'''

from collections import Counter
# cantidad de zapatos
X = int(input("Cuántos zapatos hay "))
# colección de cantidad de zapatos y total por tallas
sizes = Counter(list(map(int, input("Indica las tallas ").split())))
# Cantidad de clientes
N = int(input("Cuántos clientes "))
earned = 0

# De acuerdo a la cantidad de clientes se ejecuta el ciclo
for _ in range(N):
    # Tomo la talla y precio indicada por el cliente
    size, price = list(map(int, input(
        "Indica la talla y precio que pagas separado por un espacio ").split()))
    # Si la talla existe en la colección sumo el precio indicado por el cliente y resto 1 al stock
    if (sizes[size] > 0):
        earned += price
        sizes[size] -= 1
print(earned)
