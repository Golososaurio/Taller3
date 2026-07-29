from cargaArchivos import cargaArchivos
import random

class Punto3:
    def __init__(self):
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto3.json")

    def promedio(self):
        for i, prueba in enumerate(self.pruebas):
            suma = 0
            for nota in prueba["Notas"]:
                s1 = random.randint(0, prueba["M"] - 1)
                s2 = random.randint(0, prueba["M"] - 1)
                s3 = (nota - s1 - s2) % prueba["M"]
                suma += (s1 + s2 + s3) % prueba["M"]
            promedio = suma / len(prueba["Notas"])
            promedio = round(promedio, 1)
            print("Para las notas del estudiante " + str(i + 1) + " se tiene: \n")
            print("Luego de la reconstrucción la suma es: " + str(suma) + "\n")
            print("El promedio es: " + str(promedio) + "\n")

# NOTA: Para agregar más notas remitirse al archivo tests\punto3.json
# p = Punto3()
# pp = p.promedio() #Prueba para ver el punto 3 individualmente