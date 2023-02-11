

import textwrap


def run():
    text = input("Ingresa una cadena de texto: ")
    max_width = int(input("Ingresa el ancho de cada subcadena: "))

    def wrap(text, max_width):
        result = textwrap.fill(text, max_width)
        print(list(result))
    wrap(text, max_width)


if __name__ == '__main__':
    run()
