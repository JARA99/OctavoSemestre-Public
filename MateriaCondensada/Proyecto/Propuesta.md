#   Propuesta para codificar el proyecto

##  Descripción general

Se me ocurre repartir el código en 2 grupos principales, el de obtención de datos y el generador de gráficas.

El de obtención de datos se puede separar por distintas librerías[^1], cada una con una función específica. Y el de generar las gráficas sería bastante simple, podríamos incluso generar GIFs animados si almacenamos todos los datos y no solo los iniciales y finales.

[^1]: En Python podemos hacer "librerías", que contendrían las funciones haciendo distintos archivos ```.py``` y luego incluyéndolas en el main.

***

##  Hoja de datos

Para llevar el registro de las posiciones, velocidades y demás datos, se me ocurre usar el archivo CSV e ir agregado por bloques separados por un enter (un solo enter es importante para poder usar el comando ```every``` en gnuplot después).


##  Obtención de datos

Mi propuesta es separar este en las siguientes librerías:

*   Condiciones iniciales
*   Ecuación de movimiento
*   Interacción de nuevas posiciones
*   Conservación del momento
*   Main

### Condiciones iniciales
Esta librería debería separarse en dos funciones, una que asigne valores aleatorios a los puntos iniciales para utilizar cuando el factor de empaquetamiento es pequeño, y otra que comience con las posiciones ideales y quite una cantidad de puntos deseada. Además las funciones deben de encargarse de crear la hoja de datos ```particles.dat``` y escribir el primer bloque de datos en esta.

### Ecuación de movimiento
Esta librería debería tener una función que dado el bloque de datos del intervalo de tiempo actual, calcule la fuerza sobre cada partícula, y con esto calcule las posiciones y velocidades para el siguiente intervalo. Finalmente, que añada un bloque con estos datos a la hoja de datos.

A esta función no le debe importar si hay o si no hay un choque entre partículas o con alguna pared, de eso se encargará la siguiente librería.

### Interacción de nuevas posiciones
Esta librería se encargará de descartar los casos en los que las partículas se superpongan o traspasen las paredes. Leerá 