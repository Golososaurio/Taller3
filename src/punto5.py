from cargaArchivos import cargaArchivos
import heapq

class Punto5:
    def __init__(self):
        '''Inicialización de los atributos importantes del programa'''
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto5.json")

    def cierre(self):
        '''Toma cada caso de pruebas, carga las variables y diccionario importantes para luego
        pedir que el usuario cierre (quite) uno de los nodos, así guarda el estado de las variables
        antes del cierre y vuelve a realizar los cálculos para luego del cierre'''
        for i, prueba in enumerate(self.pruebas):
            print("Para el grafo " + str(i + 1) + ": ")
            antesCierre = {}
            rutaAnterior = {}
            for origen, destino in prueba["Pares"]:
                distancia, ruta = self.camino(prueba["Grafo"], origen, destino)
                antesCierre[(origen, destino)] = distancia
                rutaAnterior[(origen, destino)] = ruta

            primer = True
            cierre = ""
            while (cierre not in prueba["Grafo"]) or primer == True:
                print("Los nodos son los siguientes, por dónde quiere cerrar:")
                for nodo in prueba["Grafo"]:
                    print(nodo, end= " | ")
                cierre = input("\n- ")
                if cierre not in prueba["Grafo"]:
                    print("Ese nodo no está en el grafo")
                else:
                    primer = False

            del prueba["Grafo"][cierre]

            for nodo in prueba["Grafo"]:
                prueba["Grafo"][nodo] = [
                    vecino
                    for vecino in prueba["Grafo"][nodo]
                    if vecino[0] != cierre
                ]

            despuesCierre = {}
            rutaDespues = {}
            for origen, destino in prueba["Pares"]:
                if (origen not in prueba["Grafo"]) or (destino not in prueba["Grafo"]):
                    distancia, ruta = float('inf'), ["No hay camino"]
                    despuesCierre[(origen, destino)] = distancia
                    rutaDespues[(origen, destino)] = ruta
                else:
                    distancia, ruta = self.camino(prueba["Grafo"], origen, destino)
                    despuesCierre[(origen, destino)] = distancia
                    rutaDespues[(origen, destino)] = ruta

            print(f"{'Origen':<10}{'Destino':<10}{'Antes':<10}{'Después':<12}{'Diferencia':<14}{'Ruta Anterior':<14}{'Ruta Después':<14}{'Estado'}")

            for origen, destino in prueba["Pares"]:

                antesDist = antesCierre[(origen, destino)]
                despuesDist = despuesCierre[(origen, destino)]
                rutaAnt = " ".join(rutaAnterior[(origen, destino)])
                rutaDes = " ".join(rutaDespues[(origen, destino)])

                if despuesDist == float("inf"):
                    diferencia = "-"
                    estado = "Desconectado"
                else:
                    diferencia = despuesDist - antesDist
                    estado = "Aumentó" if diferencia > 0 else "Sin cambio"

                print(f"{origen:<10}{destino:<10}{antesDist:<10}{despuesDist:<12}{str(diferencia):<14}{rutaAnt:<14}{rutaDes:<14}{estado}")

    def camino(self, grafo, inicio, final):
            '''Se encarga de hacer el algoritmo Dijkstra y devolver la distancia (peso total) desde el nodo inicial
            al nodo final junto con la ruta que se toma de inicio a fin'''
            distancias = {}
            predecesores = {}
            for nodo in grafo:
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

                for vecino, peso in grafo[nodoActual]:
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
                return float('inf'), ["No hay camino"]
            else:
                return distancias[final], camino

# Mismas instrucciones del punto 4, solo es seguir la estructura del tests\punto5.json
# p = Punto5()
# pp = p.cierre() #Prueba individual para el punto 5