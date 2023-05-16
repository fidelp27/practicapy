'''
Desarrolla una clase "Carro" con atributos de marca, modelo y año. Incluye métodos para acelerar, frenar y mostrar la información del carro.
'''


class Carro():
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def __str__(self) -> str:
        print(
            f"Especificaciones del carro:\nMarca: {self.marca}\nModelo: {self.modelo}\nAño: {self.anio}\nVelocidad: {self.velocidad}")

    def checkVelocidad(self):
        print(f"Velocidad: {self.velocidad}")


carro1 = Carro("Mazda", "3", 2019)
carro1.acelerar()
carro1.checkVelocidad()
carro1.acelerar()
carro1.checkVelocidad()
carro1.acelerar()
carro1.checkVelocidad()
carro1.frenar()
carro1.frenar()
carro1.checkVelocidad()
