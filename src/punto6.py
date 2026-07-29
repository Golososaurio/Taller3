from cargaArchivos import cargaArchivos

class Punto6:
    def __init__(self):
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto6.json")

    def colorear(self):
        for i, prueba in enumerate(self.pruebas):
            print("Para la lista " + str(i + 1) + " de materias: ")
            colores = {}
            for estudiante in prueba["Materias"]:
                usados = []
                for vecino in prueba["Materias"][estudiante]:
                    if vecino in colores:
                        if colores[vecino] not in usados:
                            usados.append(colores[vecino])
                color = 0
                while color in usados:
                    color += 1
                colores[estudiante] = color
            if self.verificar(prueba["Materias"], colores) == True:
                print("Cantidad de colores:", max(colores.values()) + 1)
                for color in range(max(colores.values()) + 1):
                    print("Color", color + 1, ":", end= " ")
                    for vertice in colores:
                        if colores[vertice] == color:
                            print(vertice, end= "  ")
                    print()
            else:
                print("Ocurrió un error al colorear")

    def verificar(self, grafo, colores):
        for estudiante in grafo:
            for vecino in grafo[estudiante]:
                if colores[estudiante] == colores[vecino]:
                    return False
        return True


# p = Punto6() #Sirve para evaluar el Punto 6 en individual, para agregar más grafos, solo hay que seguir lo mismo que los anteriores puntos, es decir, la estructura
# pp = p.colorear()
