'''
Crea una clase "CuentaBancaria" con atributos de saldo y número de cuenta. Implementa métodos para depositar dinero, retirar dinero y mostrar el saldo actual.
'''


class Persona():
    def __init__(self, nombre, edad, documento):
        self.nombre = nombre
        self.edad = edad
        self.documento = documento

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'Las persona {self.nombre} tiene {self.edad} años'


class CuentaBancaria():
    def __init__(self, persona, saldo=0, numero_cuenta=''):
        if not persona.esMayorDeEdad():
            print(
                f'{persona.nombre} No puedes crear una cuenta, eres menor de edad')

        self.persona = persona
        self.saldo = saldo
        self.numero_cuenta = numero_cuenta

    def depositar(self, cantidad):
        if cantidad >= 0:
            self.saldo += cantidad
        else:
            print("Error, no puedes depositar saldos inferiores a 0")

    def extraer(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Error, no puedes extraer más dinero del que tienes")

    def consultarSaldo(self):
        print(f'El saldo actual de la cuenta es {self.saldo}')

    def __str__(self) -> str:
        return f'Ha sido creada la cuenta {self.numero_cuenta} y pertenece a {self.persona.nombre} con un saldo de {self.saldo}'


peter = Persona('Peter', 20, 95852111)
cuenta_peter = CuentaBancaria(peter, 1000, '123456789')
print(cuenta_peter)
cuenta_peter.depositar(500)
cuenta_peter.consultarSaldo()

cuenta_peter.extraer(200)
cuenta_peter.consultarSaldo()

jose = Persona('Jose', 17, 95852222)
cuenta_jose = CuentaBancaria(jose, 500, '987654321')
