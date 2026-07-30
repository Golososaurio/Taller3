from cargaArchivos import cargaArchivos

class Punto6:
    def __init__(self):
        '''Inicialización de los atributos importantes del programa'''
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto6.json")

    def colorear(self):
        '''Toma y enumera cada uno de los casos de prueba para liego pasar por cada nodo
        colocando un número (color) de 0 hasta lo que dé, sabemos que no asigna colores de más,
        pues guarda los colores usados y revisa a los vecinos del nodo que estamos mirando para
        ver cuales de los colores se han usado y así asignarle uno al nodo visto, la forma de
        asignación revisa si ya hay un vecino con color en usados, en caso de no haber ninguna
        asigna 0 como primer color al nodo que se ve, para los siguientes nodos revisa todos los
        vecinos y cuando detecta que uno tiene color lo pone en usados, luego realiza una comprobación
        desde el primer color (0) donde si no está en la lista de usados es el asignado, si está se suma
        1 simbolizando otro color, hasta que encuentra uno disponible y se lo asigna al nodo que tenemos
        seleccionado desde el principio'''
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
                print("Cantidad de colores:", max(colores.values()) + 1) #Revisa el mayor número de color y le suma 1, así no hay ningún color 0
                for color in range(max(colores.values()) + 1): 
                    print("Color", color + 1, ":", end= " ")
                    for vertice in colores:
                        if colores[vertice] == color:
                            print(vertice, end= "  ")
                    print()
            else:
                print("Ocurrió un error al colorear")

    def verificar(self, grafo, colores):
        '''Verifica que cada uno de los nodos tenga el color que le corresponde'''
        for estudiante in grafo:
            for vecino in grafo[estudiante]:
                if colores[estudiante] == colores[vecino]:
                    return False
        return True


# p = Punto6() #Sirve para evaluar el Punto 6 en individual, para agregar más grafos, solo hay que seguir lo mismo que los anteriores puntos, es decir, la estructura
# pp = p.colorear()
