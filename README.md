El siguiente programa está hecho en base a Python 3.13.

Tiene diferentes dependencias como:
    -random
    -heapq
    -json

Las cuales forman parte de la biblioteca estándar de python, por lo que
no debería de ser necesario descargarlas, pero en caso de no tenerlas se debe
descargar nuevamente python, específicamente la versión 3.13 para evitar 
conflictos con lo programado.

El programa está hecho por:
    -Daniel Alejandro Pulido Lozano

A momento de subida el archivo main.py es solo un placeholder del menú
interactivo para explorar los diferentes puntos, por lo que no es
necesaria su descarga, así que para el correcto funcionamiento del programa
se debe entrar a archivo por archivo .py en la carpeta src y descomentar los:

p = Punto#()
pp = p.metodo()

que se encuentren para ver su funcionamiento. También faltan comentarios a
momento de subida de los archivos en los métodos, pero según criterio
personal se puede entender lo que hacen los métodos con su nombre, traté
de ser lo más específico posible sin pasarme en los nombres de los métodos.

Para que los puntos puedan hacer lectura de los archivos .json de prueba si se
abre en Visual Studio Code hay que tener en cuenta que este abra con una
mesa de trabajo la cual tenga dentro una carpeta llamada Taller 3 - Discretas y
dentro estén los archivos del proyecto, la estructura debería ser del siguiente
modo:

Mesa de trabajo
|Taller 3 - Discretas
    |src
        |*Distintos archivos .py
    |tests
        |*Distintos archivos .json

No he trabajado en otros ambientes, pero supongo que deben de tener un
manejo de arcivos similar a este para el uso de los import, por este motivo
recomiendo el uso de Visual Studio Code para la visualización correcta de los
puntos del taller.

A momento de subida los archivos completos son:

    -Todos los puntos del 1 al 8
    -Todos los archivos de prueba del 1 al 8
    -Un archivo cargaArchivos.py para el manejo de pruebas para cada punto

Voy a estar realizando subidas para los puntos 9 y 10, y para agregar los
comentarios pertinentes a los métodos que se usaron.

NOTA: Este archivo puede ser modificado a futuro para la explicación de uso,
la versión original está en el commit del 29/07/2026 a las 23:55 hora Colombiana.