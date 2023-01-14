'''
The provided code stub will read in a dictionary 
containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, 
showing 2 places after the decimal.

'''


if __name__ == '__main__':
    #n = int(input("cantidad"))
    student_marks = {"Fidel": [20, 30, 40], "Eze": [30, 40, 50]}
   # for _ in range(n):
   #     name, *line = input("estudiante, nota").split()
   #     scores = list(map(float, line))
   #     student_marks[name] = scores
    query_name = input("busca")

    student = student_marks[query_name]
    avg = sum(student)/len(student)
    print("%.2f" % avg)
