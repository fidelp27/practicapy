'''
collections.namedtuple()
>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11

Dr. John Wesley has a spreadsheet containing a list of student's ID's, marks , class  and name.

Your task is to help Dr. Wesley calculate the average marks of the students.
Average = sum of all marks / total students

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N  lines contains the marks, IDs, name and class, under their respective column names.

Output Format

Print the average marks of the list corrected to 2 decimal places.
'''
from collections import namedtuple

# La primera línea recibe un número entero que indica el número total de estudiantes,
# y una cadena que contiene los nombres de las columnas separadas por espacio.
total, columns = int(input()), input().split()

# a segunda línea crea una tupla nombrada 'Student' con los nombres de las columnas
# especificadas en el input anterior.
Student = namedtuple('Student', columns)

# En la tercera línea, se usa una comprensión de listas para crear una lista de objetos 'Student',
# donde cada objeto contiene los valores separados por espacio para un estudiante específico.

# La variable _ se utiliza como una variable de contador, pero no se utilizará en ningún momento en el cuerpo del bucle.
# El operador * en Student(*input().split()) es el operador de desempaquetado de argumentos. Al utilizarlo,
# se está pasando cada elemento de la lista devuelta por input().split() como un argumento separado al
# constructor de la tupla 'Student'.
Students = [Student(*input().split()) for _ in range(total)]

# La cuarta línea imprime el promedio de las calificaciones de los estudiantes. Se
# usa una comprensión de listas para recuperar las calificaciones de cada estudiante
# y luego se divide el total de las calificaciones por el número total de estudiantes.
print("{:.2f}".format(sum([int(x.MARKS) for x in Students]) / total))
print(Students)
