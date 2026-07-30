from cargaArchivos import cargaArchivos

class Punto8:
    def __init__(self):
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto8.json")

    def simplificacion(self):
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
        diferencias = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diferencias += 1
        return diferencias == 1

    def combinar(self, a, b):
        combinacion = ""
        for i in range(3):
            if a[i] == b[i]:
                combinacion += a[i]
            else:
                combinacion += "-"
        return combinacion

    def variablePatron(self, patron):
        variables = ["A", "B", "C"]
        expresion = ""
        for i in range(len(patron)):
            if patron[i] == "1":
                expresion += variables[i]
            elif patron[i] == "0":
                expresion += "¬" + variables[i]
        return expresion

    def verificar(self, minterminos, patrones):
        correcto = True
        for mintermino in range(8):
            binario = f"{mintermino:03b}"
            original = mintermino in minterminos
            simplificada = False
            for patron in patrones:
                coincide = True
                for i in range(3):
                    if patron[i] != "-" and patron[i] != binario[i]:
                        coincide = False
                        break
                if coincide:
                    simplificada = True
                    break
            if original != simplificada:
                correcto = False
        return correcto

# p = Punto8() #Quitar el comentario para probar individualmente punto8.py
# pp = p.simplificacion()