import itertools

secuencia = itertools.count(2, 2)
print(secuencia)

for i in range(10):
    print(next(secuencia))

counter = 20

for i in itertools.count():
    if counter >= 0:
        counter -= 1
        print(i)
