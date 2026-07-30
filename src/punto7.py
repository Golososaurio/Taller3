from cargaArchivos import cargaArchivos

class Punto7:
    def __init__(self):
        archivo = cargaArchivos()
        self.pruebas = archivo.cargarArchivos("punto7.json")

    def tablaVerdad(self):
        decision = ""
        while True:
            print("Desea realizar las entradas con los tests? S/N")
            decision = input("- ")
            if decision == 'S' or decision == 'N':
                break
            else:
                ("Esa no es una opción válida")
        if decision == 'S':
            for i, prueba in enumerate(self.pruebas):
                a = prueba["Entradas"][0]
                b = prueba["Entradas"][1]
                c = prueba["Entradas"][2]
                d = prueba["Entradas"][3]
                
                print("Entrada No." + str(i+1))
                print(f"{'A':<5}{'B':<5}{'C':<5}{'D':<5}{'Resultado':<10}{'Expresion'}")
                print(f"{a:<5}{b:<5}{c:<5}{d:<5}{self.primeraExpresion(a, b, c, d):<10}{'(a and b) or (not c)'}")
                print(f"{a:<5}{b:<5}{c:<5}{d:<5}{self.segundaExpresion(a, b, c, d):<10}{'(a xor b) and c'}")
                print(f"{a:<5}{b:<5}{c:<5}{d:<5}{self.terceraExpresion(a, b, c, d):<10}{'(a or b) and ((not a) or c)'}")
        else:
            print('\n(a and b) or (not c)')
            print(f"{'A':<5}{'B':<5}{'C':<5}{'D':<5}{'Resultado':<10}")
            for a in [True, False]:
                for b in [True, False]:
                    for c in [True, False]:
                        for d in [True, False]:
                            print(f"{a:<5}{b:<5}{c:<5}{d:<5}{self.primeraExpresion(a, b, c, d):<10}")

            print('\n(a != b) and c')
            print(f"{'A':<5}{'B':<5}{'C':<5}{'D':<5}{'Resultado':<10}")
            for a in [True, False]:
                            for b in [True, False]:
                                for c in [True, False]:
                                    for d in [True, False]:
                                        print(f"{a:<5}{b:<5}{c:<5}{d:<5}{self.segundaExpresion(a, b, c, d):<10}")

            print('\n((a or b) and ((not a) or c)')
            print(f"{'A':<5}{'B':<5}{'C':<5}{'D':<5}{'Resultado':<10}")
            for a in [True, False]:
                            for b in [True, False]:
                                for c in [True, False]:
                                    for d in [True, False]:
                                        print(f"{a:<5}{b:<5}{c:<5}{d:<5}{self.terceraExpresion(a, b, c, d):<10}")


    def primeraExpresion(self, a, b, c, d):
        return (a and b) or (not c)

    def segundaExpresion(self, a, b, c, d):
        return (a != b) and c

    def terceraExpresion(self, a, b, c, d):
        return (a or b) and ((not a) or c)

# p = Punto7() #Para iniciar individualmente el Punto 7
# pp = p.tablaVerdad()