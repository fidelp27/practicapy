'''
Crear una clase "Rectángulo" con atributos de longitud y ancho. Incluye métodos para calcular el área y el perímetro del rectángulo.
'''


class Rectangulo():
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

    def calcular_perimetro(self):
        return 2 * (self.largo + self.ancho)

    def __str__(self) -> str:
        return f'El rectángulo tiene un largo de {self.largo} y un ancho de {self.ancho}'


if __name__ == '__main__':
    rectangulo = Rectangulo(10, 5)
    print(rectangulo)
    print(f'El área del rectángulo es {rectangulo.calcular_area()}')
    print(
        f'El perímetro del rectángulo es {rectangulo.calcular_perimetro()}')
