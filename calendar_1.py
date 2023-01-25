from datetime import datetime
import calendar
from calendar import TextCalendar

cal = calendar.Calendar()

# Devuelve el mes
mes = calendar.month(2022, 1)
print(mes)

'''
    January 2022
Mo Tu We Th Fr Sa Su
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30
31
'''
# Lista de días del mes separado por semanas
lista_semanas_mes = calendar.monthcalendar(2022, 1)
print(lista_semanas_mes)
# [[0, 0, 0, 0, 0, 1, 2], [3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16], [17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30], [31, 0, 0, 0, 0, 0, 0]]


# Semana en que se encuentra el día indicado
semana = calendar.weekday(2022, 2, 27)
print("semana: ", semana)

# Día que corresponde a la fecha indicada

dia = calendar.weekday(2022, 2, 28)
print("dia: ", dia)

# Devuelve True o False si el año indicado es bisiesto
bisiesto = calendar.isleap(2022)
print(bisiesto)


cal = TextCalendar()
# Devuelve un mes calendario
mes = cal.prmonth(2022, 3)


# *********************************Solución larga**********************
d = calendar.weekday(2023, 1, 25)
days = ["DOMINGO", "LUNES", "MARTES",
        "MIERCOLES", "JUEVES", "VIERNES", "SABADO"]
print(days[d])


dias = ["LUNES", "MARTES",
        "MIERCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO"]

fecha = list(map(int, input().split()))
mes, dia, anio = fecha
print(anio, mes, dia)

week_day = calendar.weekday(anio, mes, dia)
print(dias[week_day])

# ***************************Solución corta ****************************
m, d, y = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
