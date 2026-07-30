from cargaArchivos import cargaArchivos

class Punto1:
    def __init__(self):
        '''Inicialización de los atributos importantes del programa'''
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto1.json")
        self.mayusculas = (65, 90)
        self.minMayusculas, self.maxMayusculas = self.mayusculas
        self.minusculas = (97, 122)
        self.minMinusculas, self.maxMinusculas = self.minusculas

    def cifrarTexto(self):
        '''Se encarga de traer cada prueba desde la carpeta tests, toma el código revisa cuales de los caracteres
        es una letra, si es una letra la pasa por el desplazamiento establecido como es cifrado se encarga de sumar
        dicho desplazamiento y luego revisa que no se salga de los límites de los caracteres en ASCII, también 
        pregunta si se conoce el texto esperado para saber si hace la comprobación dentro del archivo punto1.json'''
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
        '''Se encarga de traer cada prueba desde la carpeta tests, toma el código revisa cuales de los caracteres
        es una letra, si es una letra la pasa por el desplazamiento establecido como es descifrado se encarga de
        restar dicho desplazamiento y luego revisa que no se salga de los límites de los caracteres en ASCII,
        también pregunta si se conoce el texto esperado para saber si hace la comprobación dentro del archivo punto1.json'''
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
        '''Toma el texto que se le envie y hace todos los descifrados posibles en el alfabeto ingles e imprime dichos
        descifrados para que el usuario vea cuál entre todos ellos puede ser el texto que está buscando'''
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
            print("El descifrado para un desplazamiento de " + str(i) + " es: " + textoCifrado)


# Nota: Para que los 2 primeros métodos hagan su tarea con otras pruebas, agregarlas en tests\punto1.json como están las demás en el mismo archivo 
# p = Punto1()
# pp = p.cifrarTexto() #Prueba de cifrarTexto
# pp = p.descifrarTexto() #Prueba de descifrarTexto
# pp = p.descifrarFuerza("KROD XQDO") #Prueba de descifrarFuerza cambiar texto entre comillas para probar distintos con distintos textos cifrados