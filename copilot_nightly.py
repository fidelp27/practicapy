'''
Hagamos una prueba de copilot con un archivo de python para hacer un llamado a una API cualquiera y traer los datos de la misma.
'''
# importo requests para hacer el llamado a la API
import requests


def getdata(url):
    # un bloque try except para manejar errores
    try:
        data = requests.get(url)
        print(data.json())
        return data.json()
    except Exception as e:
        print(e)
        return None


# ejecutar como modulo
if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/todos'
    getdata(url)
