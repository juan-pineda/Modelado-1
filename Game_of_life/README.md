
Yeison Fabián Santos:
juego_de_la_vida_yeison.py

* La solución está bien, y la implementación relativamente limpia, sin excesivo ruido 
* Bien por usar comentarios, pero deberían ser más y más explícitos para poder entender bien
* Hay que depurar el código, borrando las líneas que no se necesitan
* Usar funciones vectorizadas para evitar los loops for
* Las variables globales se deben evitar al máximo
* Para entender cómo hacer rodar la animación, ver la solución de Andrés Felipe Jerez
* Me parece que su implementación asume condiciones de contorno periódicas... es así?

*********************************************

Andrés Felipe Jerez Ariza:
https://github.com/anfejear/Life-s-game

* Bien por comenzar con la descripción general
* Bien por el uso de comentarios y por separa el código en bloques para poder seguirlo
* Bien por el uso de funciones. La próxima vez, documentarlas según el estándar con DocStrings ”””
* Buena solución con la convolución
* Hay que tener cuidado con el uso de las variables globales, pues pueden inducir a errores. Tratar de usarlas solamente cuando sea necesario
* Bien por el uso de la animación

*********************************************
Diego Rueda:
https://github.com/druedaplata/masterMath/tree/master/class/math_modelling_1/lifes_game

* Excelente trabajo.
* Faltó hacer el estudio del comportamiento del juego, explorarlo.

*********************************************
Andres David Guerrero Duran:
lifes_game_ADGD.zip

* Bien por separar en bloques, y por ir documentando los pasos con las figuras y todo
* Faltó explicar el problema y la estrategia general al comienzo
* Para generar enteros podría usar np.random.randint()
* vecinos=np.zeros((M,N), dtype=int) podria cambiarse por vecinos=np.zeros(initial.shape, dtype=int)
* Buen uso de numpy y de evaluación de condiciones lógicas


*********************************************
Jorge L. Rodríguez Donado:
Game of life_JLRD.ipynb 

* Faltó utilizar las ventajas de markdown para documentar y exponer su propuesta, explicándole al lector qué es lo que tiene ante él.
* Faltó hacer una propuesta más allá de simplemente programar los pasos
* Usar funciones vectorizadas para evitar los ciclos 'for'

* [Err ] No such file or directory: '/home/jorgerd/Escritorio/Figura/matriz0.jpg'
* Utilizar paths relativos, o definir al inicio una variable, de modo que podamos cambiarla una sola vez 

* Agregar comentarios para saber qué es cada variable, y qué pretende lograr en cada paso
* Separar las celdas haría más fácil testarlo

* Buen uso del slicing al extraer/modificar partes de las matrices

* Para sumar todos los elementos de una matriz, usar el método .sum()
* Buen uso de las imágenes para crear el gif
* Bien por el uso amplio de comentarios
* Bien por documentar el uso de nu paquete externo para que podamos entender cómo procedió
