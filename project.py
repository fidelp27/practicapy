def get_bisiestos(year):
    bisiestos = []
    for i in range(year+1):
        if i % 4 == 0 and (i % 400 == 0 or i % 100 != 0):
            bisiestos.append(i)
    print(len(bisiestos))
    return bisiestos
