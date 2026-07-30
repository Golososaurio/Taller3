from cargaArchivos import cargaArchivos
import heapq

class Punto4:
    def __init__(self):
        '''Inicialización de los atributos importantes del programa'''
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto4.json")

    def camino(self):
        '''Realiza el algoritmo Dijkstra para buscar el camino de un punto A a un punto B
        que se dejan a elección del usuario'''
        for i, prueba in enumerate(self.pruebas):
            print("Para el grafo " + str(i + 1) + ": ")
            primer = True #Funciona para que entre sí o sí en un primer momento al while
            inicio = ""
            final = ""
            while (inicio not in prueba["Grafo"]) or (final not in prueba["Grafo"]) or primer == True:
                print("Los nodos son los siguientes, por dónde quiere iniciar:")
                for nodo in prueba["Grafo"]:
                    print(nodo, end= " | ")
                inicio = input("\n- ")
                if inicio not in prueba["Grafo"]:
                    print("Ese nodo no está en el grafo")
                else:
                    print("Cúal es el nodo final?")
                    final = input("- ")
                    if final not in prueba["Grafo"]:
                        print("Ese nodo no está en el grafo")
                    else:
                        primer = False
                
            distancias = {}
            predecesores = {}
            for nodo in prueba["Grafo"]:
                distancias[nodo] = float('inf')
                predecesores[nodo] = None
            distancias[inicio] = 0

            colaPrioridad = [(0, inicio)] #distancia con el nodo inicial
            while colaPrioridad:
                distanciaActual, nodoActual = heapq.heappop(colaPrioridad)

                if nodoActual == final:
                    break

                if distanciaActual > distancias[nodoActual]:
                    continue

                for vecino, peso in prueba["Grafo"][nodoActual]:
                    distancia = distanciaActual + peso

                    if distancia < distancias[vecino]:
                        distancias[vecino] = distancia
                        predecesores[vecino] = nodoActual
                        heapq.heappush(colaPrioridad, (distancia, vecino))

            camino = []
            nodoActualCamino = final

            while nodoActualCamino is not None:
                camino.insert(0, nodoActualCamino)
                nodoActualCamino = predecesores[nodoActualCamino]

            if camino[0] != inicio:
                print("No hay camino")
            else:
                print("La distancia es: " + str(distancias[final]) + ".\nLa ruta óptima es: " + " ".join(camino) + "\n")

# NOTA: Si bien los nodos son solo letras es para hacer más sencillo el probarlas, puede nombrarlas como desee en
# el archivo tests\punto4.json mientras tengan la estructura propuesta y a la hora de correr el programa
# el nombre que ingrese sea correcto.
# p = Punto4()
# pp = p.camino() #Prueba individual para el punto 4