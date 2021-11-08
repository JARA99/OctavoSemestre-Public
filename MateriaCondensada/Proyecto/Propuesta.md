#   Propuesta para codificar el proyecto

##  Descripción general

Se me ocurre repartir el código en 2 grupos principales, el de obtención de datos y el generador de gráficas.

El de obtención de datos se puede separar por distintas librerías[^1], cada una con una función específica. Y el de generar las gráficas sería bastante simple, podríamos incluso generar GIFs animados si almacenamos todos los datos y no solo los iniciales y finales.

[^1]: En Python podemos hacer "librerías", que contendrían las funciones haciendo distintos archivos ```.py``` y luego incluyéndolas en el main.

***

##  Obtención de datos

Mi propuesta es separar este en las siguientes librerías

### Condiciones iniciales [dos librerías]
