from cargaArchivos import cargaArchivos

class Punto8:
    def __init__(self):
        '''Inicialización de los atributos importantes del programa'''
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto8.json")

    def simplificacion(self):
        '''Toma y enumera cada una de las pruebas del archivo de pruebas para luego
        hacer uso de los diferentes métodos para dar una expresión simplificada, y para
        finalizar revisa si la expresión simplificada es correcta'''
        for i, prueba in enumerate(self.pruebas):
            print("Para el grupo " + str(i+1) + " de minterminos:")
            minterminos = []
            for numero in prueba["Minterminos"]:
                minterminos.append(f"{numero:03b}")
            while True:
                combinaciones = []
                for i in range(len(minterminos)):
                    for j in range(i + 1, len(minterminos)):
                        if self.diferencia(minterminos[i], minterminos[j]):
                            combinacion = self.combinar(minterminos[i], minterminos[j])
                            if combinacion not in combinaciones:
                                combinaciones.append(combinacion)
                if len(combinaciones) == 0:
                    break
                minterminos = combinaciones
            print("Patrones obtenidos:")
            for patron in minterminos:
                print(patron)
            print("Expresión simplificada:")
            for patron in minterminos:
                print(self.variablePatron(patron))
            if self.verificar(prueba["Minterminos"], minterminos):
                print("La simplificación es correcta.")
            else:
                print("La simplificación NO es correcta.")

    def diferencia(self, a, b):
        '''Busca diferencias entre a y b, si las diferencias que tienen
        es exactamente 1, devuelve un True'''
        diferencias = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diferencias += 1
        return diferencias == 1

    def combinar(self, a, b):
        '''Busca en cada caracter de a y b en misma posicion si son iguales, en caso de que lo sean
        deja el caracter de a como está, si son diferentes agrega un caracte _ para simbolizar que
        no importa'''
        combinacion = ""
        for i in range(3):
            if a[i] == b[i]:
                combinacion += a[i]
            else:
                combinacion += "-"
        return combinacion

    def variablePatron(self, patron):
        '''Se encarga de traducir el patron a la forma que se desea, así pasa por todas las posiciones
        del patron, que al ser solo 3 se pueden corresponder con A, B y C, respectivamente, si es 1
        agrega la variable en posicion del 1 en el patron, caso que sea un 0 devuelve un ¬ junto con 
        la variable, cualquier otro caracter es ignorado'''
        variables = ["A", "B", "C"]
        expresion = ""
        for i in range(len(patron)):
            if patron[i] == "1":
                expresion += variables[i]
            elif patron[i] == "0":
                expresion += "¬" + variables[i]
        return expresion

    def verificar(self, minterminos, patrones):
        '''Revisa que alguno de los minterminos se pueda relacionar con los patrones simplificados'''
        correcto = True
        for mintermino in range(8): #Toma un mintermino entre 0 a 7
            binario = f"{mintermino:03b}" #Transforma el mintermino a binario de 3 variables
            original = mintermino in minterminos #Revisa que el mintermino esté en la lista de minterminos original, si es así da True, caso contrario False
            simplificada = False #Estado base de simplificada
            for patron in patrones: #Busca en cada patrón guardado en patrones
                coincide = True #Estado base de coincide
                for i in range(3):
                    if patron[i] != "-" and patron[i] != binario[i]: #Revisa las 3 variables del patron y el binario del mintermino seleccionado y los compara
                        coincide = False #Si no coinciden en algún punto el patron con el binario del mintermino se devuelve un false y se rompe el for
                        break
                if coincide: #Si coincide se mantiene en True se da como que el patron ya está simplificado
                    simplificada = True
                    break
            if original != simplificada: #Si en algún punto la expresión simplificada es distinta a la original se da como que la simplificación estuvo errada
                correcto = False
        return correcto

# p = Punto8() #Quitar el comentario para probar individualmente punto8.py
# pp = p.simplificacion()