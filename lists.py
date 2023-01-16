'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of commands where each command will 
be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
'''

if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        func, *args = input().split()
        if func != 'print':
            getattr(lst, func)(*map(int, args))
        else:
            print(lst)

'''
1) La primera línea if __name__ == '__main__': es una verificación para
asegurar que el código solo se ejecutará si el archivo en el que se encuentra 
este código es el archivo principal que se está ejecutando.

2) La línea N = int(input()) obtiene un número entero del usuario a través del teclado,
que se utilizará como el número de iteraciones para el bucle for.

3) La línea lst = [] crea una lista vacía llamada "lst" que se utilizará en las operaciones posteriores.

4) El bucle for _ in range(N): se ejecutará N veces, en cada iteración se pedirá al usuario ingresar 
una línea de texto que contiene el nombre de un método y uno o varios argumentos separados por espacios.

5) La línea func, *args = input().split() toma la entrada del usuario, la divide en una lista utilizando 
el método split() y asigna el primer elemento a la variable "func" y los demás elementos a la lista "args".

    5.1) *args es una notación comúnmente utilizada en Python para pasar un número variable de argumentos a una función.

    5.2) La notación "*" antes del nombre de la variable indica que esta variable es una 
    tupla (o una lista) que recoge todos los argumentos adicionales que no han sido asignados 
    a variables específicas en el orden en que fueron pasados.

    5.3) En el caso del ejemplo anterior func, *args = input().split(), "*args" significa que
    se recogen todos los elementos de la lista resultante del método split() en una tupla 
    llamada "args", excepto el primer elemento que se asigna a la variable "func".

6) La línea if func != 'print': verifica si la entrada del usuario es diferente a "print", si es asi entonces, 
se utiliza la función getattr para obtener el método con el nombre almacenado en la variable "func" del objeto "lst" 

7) La función getattr recibe dos argumentos, el primer argumento es el objeto al que 
se quiere acceder, el segundo argumento es el nombre del método o atributo como string

8) La función *map(int, args) toma cada elemento de la lista "args" y los convierte en números enteros.

9) La función getattr(lst, func)(*map(int, args)) se utiliza para llamar al método del objeto "lst" con el
nombre almacenado en la variable "func" y los argumentos convertidos en enteros.
    9.1) La expresión getattr(lst, func)(*map(int, args)) es una forma 
    de llamar un método de un objeto de forma dinámica en Python.
    9.2) La función getattr(objeto, nombre_metodo) recibe dos argumentos:
        9.2.1) objeto: es el objeto en el cual se quiere acceder.
        9.2.2) nombre_método: es un string con el nombre del método o atributo que se quiere obtener.
    9.3) En este caso getattr(lst, func) regresa el método del objeto "lst" con el nombre almacenado en la variable "func"
    9.4) La función *map(func, iterable) aplica la función "func" a cada elemento del 
    iterable (en este caso es la lista "args") y devuelve un objeto iterable
    9.5) En este caso map(int, args) convierte cada elemento de la lista "args" en un número entero.
    9.6) La expresión *map(int, args) desempaqueta el objeto iterable resultante de la función map y 
    pasa cada elemento como un argumento individual al método obtenido por getattr(lst, func).
10) Por último, si el usuario ingresa "print", se imprime la lista "lst" utilizando print(lst)


'''
