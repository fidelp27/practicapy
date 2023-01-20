def get_permuted(str):
    lista = list(str)
    lista2 = []
    for i in lista:
        for j in lista:
            lista2.append(sorted([i, j]))
    lista2.sort()
    for i in lista2:
        if i[0] != i[1]:
            print("".join(i))


get_permuted("HACK")
