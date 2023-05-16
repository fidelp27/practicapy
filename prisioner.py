'''
A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.
Example:
n = 4
m = 6
s = 2
There are 4 prisoners, 6 pieces of candy and distribution starts at chair 2. The prisoners arrange themselves in seats numbered 1 to 4. Prisoners receive candy at positions 2,3,4,1,2,3. The prisoner to be warned sits in chair number 3.
'''


def saveThePrisoner(n, m, s):
    # Write your code here
    return ((s - 1) + m - 1) % n + 1


'''
(s - 1): Restamos 1 a la posición inicial s para obtener el índice base, ya que en Python los índices de las listas comienzan desde 0.

+ m - 1: Le sumamos m - 1 al índice base para avanzar m - 1 posiciones adicionales. Esto representa la cantidad de dulces que se distribuirán menos 1, ya que el último dulce se asignará al prisionero que tenga el índice calculado.

% n: Utilizamos el operador módulo % para asegurarnos de que el índice esté dentro de los límites de la cantidad total de prisioneros n. Si el índice calculado excede n - 1, el operador módulo lo ajustará para que esté en el rango válido.

+ 1: Sumamos 1 al índice calculado para obtener el número de prisionero correspondiente. Esto se debe a que en la fórmula anterior utilizamos índices basados en 0, pero en el contexto del problema, los prisioneros están numerados desde 1 hasta n.
'''
