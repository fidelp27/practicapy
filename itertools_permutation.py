from itertools import permutations
# se utiliza para obtener dos valores de entrada del usuario,
# separados por un espacio, y almacenarlos en las variables "S" y "K",
S, K = input("Palabra y cantidad de caracteres en el grupo").split()


print(*["".join(i) for i in sorted(list(permutations(S, int(K))))], sep='\n')
'''
La función "permutations" toma dos argumentos, la primera es la 
cadena "S" y segundo es el entero "K", que indica el número de caracteres que se 
utilizarán para cada permutación. La función devuelve un objeto iterable de tuplas, 
donde cada tupla contiene una permutación posible.

La función "sorted" se utiliza para ordenar las permutaciones en orden alfabético.

La función "list" se utiliza para convertir el objeto iterable de tuplas en una lista de tuplas.

La expresión "".join(i) se utiliza para unir los caracteres de cada tupla 
en una sola cadena, cada una de estas cadenas se agrega a una lista.

se utiliza para desempaquetar los elementos de la lista resultante de la expresión 
de comprensión de listas, para que cada uno de los elementos sea impreso en una línea 
separada. Sin el operador *, se imprimiría la lista completa en una sola línea.

La expresión "print([...], sep = '\n')" se utiliza para imprimir cada cadena 
de la lista en una línea nueva. El carácter "" antes de la lista indica que se 
deben desempaquetar los elementos de la lista antes de pasarlos como argumentos
a la función "print". El argumento "sep='\n'" se 
utiliza para indicar que se debe utilizar un salto de línea como separador entre los elementos impresos.
'''
