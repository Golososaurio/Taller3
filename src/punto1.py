from cargaArchivos import cargaArchivos

class Punto1:
    def __init__(self):
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto1.json")
        self.mayusculas = (65, 90)
        self.minMayusculas, self.maxMayusculas = self.mayusculas
        self.minusculas = (97, 122)
        self.minMinusculas, self.maxMinusculas = self.minusculas

    def cifrarTexto(self):
        for prueba in self.pruebas:
            textoCifrado = ""
            if prueba["Cifrado"] == 1:
                for caracter in prueba["Codigo"]:
                    if caracter.isalpha():
                        numeroCaracter = ord(caracter)
                        numeroCaracter += prueba["Desplazamiento"]
                        if self.minMayusculas <= numeroCaracter <= self.maxMayusculas or self.minMinusculas <= numeroCaracter <= self.maxMinusculas:
                            textoCifrado += chr(numeroCaracter)
                        else:
                            numeroCaracter -= 26
                            textoCifrado += chr(numeroCaracter)
                    else:
                        textoCifrado += caracter
                while True:
                    decision = input("¿Ya conoce el texto esperado? S/N\n")
                    if decision == "S":
                        if textoCifrado == prueba["Esperado"]:
                            print("El cifrado esperado es: " + textoCifrado)
                            break
                    elif decision == "N":
                        print("El cifrado fue exitoso: " + textoCifrado)
                        break
                    else:
                        print("Esa no es una opción válida")

    def descifrarTexto(self):
        for prueba in self.pruebas:
            textoCifrado = ""
            if prueba["Cifrado"] == 0:
                for caracter in prueba["Codigo"]:
                    if caracter.isalpha():
                        numeroCaracter = ord(caracter)
                        numeroCaracter -= prueba["Desplazamiento"]
                        if self.minMayusculas <= numeroCaracter <= self.maxMayusculas or self.minMinusculas <= numeroCaracter <= self.maxMinusculas:
                            textoCifrado += chr(numeroCaracter)
                        else:
                            numeroCaracter += 26
                            textoCifrado += chr(numeroCaracter)
                    else:
                        textoCifrado += caracter
                while True:
                    decision = input("¿Ya conoce el texto esperado? S/N\n")
                    if decision == "S":
                        if textoCifrado == prueba["Esperado"]:
                            print("El descifrado esperado es: " + textoCifrado)
                            break
                    elif decision == "N":
                        print("El descifrado fue exitoso: " + textoCifrado)
                        break
                    else:
                        print("Esa no es una opción válida")

    def descifrarFuerza(self, texto):
        print("Estos son los posibles descifrados: \n")
        for desplazamiento in range(26):
            textoCifrado = ""
            for caracter in texto:
                if caracter.isalpha():
                    numeroCaracter = ord(caracter)
                    numeroCaracter -= desplazamiento + 1
                    if self.minMayusculas <= numeroCaracter <= self.maxMayusculas or self.minMinusculas <= numeroCaracter <= self.maxMinusculas:
                        textoCifrado += chr(numeroCaracter)
                    else:
                        numeroCaracter += 26
                        textoCifrado += chr(numeroCaracter)
                else:
                    textoCifrado += caracter
            i = desplazamiento + 1
            print("El descifrado para un desplazamiento de " + str(i) + " es: " + textoCifrado + "\n")

p = Punto1()
pp = p.descifrarFuerza("KROD XQDO")