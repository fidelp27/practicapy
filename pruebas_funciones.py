N = int(input("Cuántas operaciones harás"))
lst = []
for _ in range(N):
    # Devuelve una lista
    # *args Devuelve una lista con en donde el primer argumento va a func y el resto se queda en una lista
    func, *args = input("Dame el método y argumentos").split()
    if func != "print":
        # getattr devuelve un atributo de un objeto especifico
        # *map recorre todo args y lo convierte a entero
        # La expresión *map(int, args) desempaqueta el objeto iterable resultante de la función map y pasa cada elemento como un argumento individual al método obtenido por getattr(lst, func).
        # "*" es un operador especial que ayuda a "getattr" a ejecutar la función con los argumentos convertidos en números enteros.
        getattr(lst, func)(*map(int, args))
        print(lst)
        print(func)
        print(args)
    else:
        print(lst)

# Los parámetros deben ir de acuerdo a la funcion ejecutada
# append recibe solo un parámetro
# insert recibe 2
