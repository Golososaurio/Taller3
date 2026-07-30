from cargaArchivos import cargaArchivos
import random

class Punto3:
    def __init__(self):
        '''Inicialización de los atributos importantes del programa'''
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto3.json")

    def promedio(self):
        '''Trae cada caso de prueba de tests, luego para cada nota que esté disponible
        desde el caso de prueba saca un s1 y s2 con la biblioteca random que sean iguales
        a un número aleatorio desde 0 hasta el M-1 elegido, luego mediante una ecuación se
        obtiene un s3, en esencia s1, s2 y s3 son únicos para cada nota, luego se suma, usando
        dichos s1, s2 y s3 junto con M para obtener la nota, finalmente se promedia y se nos
        da el promedio del estudiante, la nota solo la sabe la variable nota, pues se debe
        traer para realizar el cifrado'''
        for i, prueba in enumerate(self.pruebas):
            suma = 0
            for nota in prueba["Notas"]:
                s1 = random.randint(0, prueba["M"] - 1)
                s2 = random.randint(0, prueba["M"] - 1)
                s3 = (nota - s1 - s2) % prueba["M"]
                suma += (s1 + s2 + s3) % prueba["M"]
            promedio = suma / len(prueba["Notas"])
            promedio = round(promedio, 1)
            print("Para las notas del estudiante " + str(i + 1) + " se tiene: ")
            print("Luego de la reconstrucción la suma es: " + str(suma))
            print("El promedio es: " + str(promedio) + "\n")

# NOTA: Para agregar más notas remitirse al archivo tests\punto3.json
# p = Punto3()
# pp = p.promedio() #Prueba para ver el punto 3 individualmente