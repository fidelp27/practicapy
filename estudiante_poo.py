'''
Implementa una clase "Estudiante" con atributos de nombre, edad y calificaciones. Incluye métodos para calcular el promedio de calificaciones y determinar si el estudiante está aprobado (promedio mayor o igual a 70).
'''


class Estudiante():
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

    def esta_aprobado(self):
        if self.calcular_promedio() >= 70:
            return "Aprobado"
        else:
            return "Reprobado"

    def __str__(self) -> str:
        return f'El estudiante {self.nombre} tiene {self.edad} años y sus calificaciones son {self.calificaciones}'


if __name__ == '__main__':
    estudiante = Estudiante('Juan', 20, [80, 70, 60])
    print(estudiante)
    print(f'El promedio del estudiante es {estudiante.calcular_promedio()}')
    print(f'El estudiante está aprobado? {estudiante.esta_aprobado()}')
