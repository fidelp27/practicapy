'''
Resolución de ejercicios de comprensión. Ejercicios otorgados por chatGPT
'''
import re
#!Dada una lista de números, crea una nueva lista que contenga sólo los números impares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numeros = [numero for numero in numeros if numero % 2 != 0]
print(new_numeros)

#!Dada una lista de cadenas de caracteres, crea una nueva lista que contenga sólo las cadenas de caracteres que
#! empiezan con la letra "a".

palabras = ["hola", "adiós", "amigo", "aire", "bote"]
new_palabras = [palabra for palabra in palabras if palabra[0] == "a"]
print(new_palabras)

#!Dada una lista de diccionarios que contienen nombres y edades, crea una nueva lista que contenga sólo los nombres.
personas = [{"nombre": "Juan", "edad": 25}, {"nombre": "Ana", "edad": 17}, {
    "nombre": "Pedro", "edad": 32}, {"nombre": "María", "edad": 15}]
new_personas = {persona["nombre"] for persona in personas}
print(new_personas)

#!Dada una lista de cadenas de caracteres, crea una nueva lista que contenga sólo las cadenas de
#! caracteres que contienen la letra "o".
palabras_full = ["hola", "adiós", "amigo", "aire", "bote"]
new_palabras_con_o = [
    palabra for palabra in palabras_full if re.search(r"\b\w*[oó]\w*\b", palabra, flags=re.IGNORECASE)]
print(new_palabras_con_o)

#!Dado un diccionario que contiene nombres y edades, crea una nueva lista que contenga sólo los nombres
#! de las personas que tienen una edad par.

personas = {"Juan": 25, "Ana": 17, "Pedro": 32, "María": 15}
new_personas_pares = [
    persona for persona in personas if personas[persona] % 2 == 0]
print(new_personas_pares)

#!Dada una lista de números, crea una nueva lista que contenga sólo los números mayores que 10 y menores que 20.
numeros_full = [5, 15, 10, 20, 25, 30]
new_numeros_filtered = [
    numero for numero in numeros_full if numero > 10 and numero < 20]
print(new_numeros_filtered)

#!Dada una lista de cadenas de caracteres, crea una nueva lista que contenga sólo las cadenas de caracteres
#! que tengan una longitud mayor que 3 y que empiecen con la letra "a".

palabras_to_filter = ["hola", "adiós", "amigo", "aire", "bote"]
new_palabras_filtered = [palabra for palabra in palabras_to_filter if len(
    palabra) > 3 and palabra.startswith("a")]
print(new_palabras_filtered)

#!Dado un diccionario que contiene nombres y edades, crea una nueva lista que contenga sólo los nombres de
#! las personas que tienen más de 20 años.

personas_a_filtrar = {"Juan": 25, "Ana": 17, "Pedro": 32, "María": 15}
new_personas_greatertwenty = [
    persona for persona in personas_a_filtrar if personas_a_filtrar[persona] > 20]
print(new_personas_greatertwenty)


'''
1) Crea una lista de tuplas donde cada tupla contiene el índice y el valor correspondiente de una lista dada.

2) Crea una lista de todos los números impares entre 1 y 50 que no sean múltiplos de 3.

3) Dada una lista de palabras, crea una lista de tuplas donde cada tupla contiene una palabra y la longitud de esa palabra.

4) Dada una lista de números, crea una lista que contenga solo los números que son divisibles por el primer elemento de la lista.

5) Dadas dos listas de números del mismo tamaño, crea una lista de tuplas donde cada tupla contiene un número de la primera lista y su correspondiente número de la segunda lista.
'''
