import json
import os

class cargaArchivos:
    def existenciaArchivo(self, ruta):
        '''Se encarga de revisar que la ruta dada exista y devuelve el booleano correspondiente'''
        if os.path.exists(ruta):
            return True
        else:
            return False

    def cargarArchivos(self, archivo):
        '''Si el archivo existe intenta abrirlo y guardar todas las pruebas en una variable'''
        ruta = os.path.join("Taller 3 - Discretas", "tests", archivo)
        existenciaArchivo = self.existenciaArchivo(ruta)
        if existenciaArchivo == True:
            try:
                with open(ruta, 'r') as file:  #Carga el archivo de tests .json
                    self.archivo = json.load(file)
                    archivo = self.archivo["Pruebas"]
                    return archivo
            except:
                return "No se pudo cargar el archivo, remítase al repositorio"
        else:
            return "No existen las pruebas, remítase al repositorio"


# Para probar funcionamiento descomentar las siguientes 3 líneas
# p = cargaArchivos()
# pp = p.cargarArchivos("punto1.json")
# print(pp)