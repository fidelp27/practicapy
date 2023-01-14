'''
Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line

Example:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Output:
Berry
Harry
'''
# Saqué los inputs para facilitar el testeo de la solución

if __name__ == '__main__':
    lista = [['Fidel', 3.3], ['Ivon', 5.6], [
        'Eze', 5.4], ["Juan", 5.4], ["Pedro", 3.5]]

    # for n in range(int(input())):
    # print(n)
    # name = input("Dame el nombre")
    # score = float(input("Dime la calificacion"))
    # lista.append([name, score])
    lista_ordenada = sorted(lista, key=lambda student: student[1])
    min_note = min(lista_ordenada, key=lambda student: student[1])[1]
    lista_filtrada = list(filter(
        lambda student: student[1] > min_note, lista_ordenada))
    min_note = min(lista_filtrada, key=lambda student: student[1])[1]
    lista_filtrada_ultima = list(
        filter(lambda student: student[1] == min_note, lista_filtrada))
    lista_final = sorted(lista_filtrada_ultima)
    for participante in lista_final:
        print(participante[0])
