from cargaArchivos import cargaArchivos

class Punto2:
    def __init__(self):
        '''Inicialización de los atributos importantes del programa'''
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto2.json")

    def descifrar(self):
        '''Toma cada prueba de la carpeta tests, luego se encarga de declarar las varibles
        y así llamar las demás funciones para realizar el descifrado'''
        for prueba in self.pruebas:
            p = prueba["P"]
            q = prueba["Q"]
            e = prueba["E"]
            m = prueba["M"]
            n = p * q
            phi = (p - 1) * (q - 1)
            if self.comprobarExponente(phi, e) == True:
                d = 0
                for x in range (1, phi):
                    if (x * e) % phi == 1:
                        d = x
                        break
                cifrado = self.euclidesExtendido(m, e, n)
                descifrado = self.euclidesExtendido(cifrado, d, n)
                if descifrado == m:
                    print("El mensaje es correcto con el esperado: " + str(descifrado))
                else:
                    print("El mensaje no es el correcto con el esperado: " + str(descifrado))
            else:
                print("El exponente público no es válido, porque no posee inverso modular\n")


    def comprobarExponente(self, phi, e):
        '''Comprueba que el exponente público sea válido (Tenga inverso modular)'''
        a = phi
        b = e
        while b != 0:
            a, b = b, a % b
        if a == 1:
            return True
        else:
            return False

    def euclidesExtendido(self, a, b, c):
        '''Nos da el inverso modular de a**b'''
        a = a ** b
        for x in range(1, c):
            if (x * a) % c == 1:
                return x

# p = Punto2() 
# pp = p.comprobarExponente(3120, 17) #Prueba para ver si la comprobación está funcionando
# print(pp)
# pp = p.descifrar() #Prueba del descrifrado del punto 2, para agregar más seguir la estructura en tests\punto2.json