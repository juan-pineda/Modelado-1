# Readme files using markdown

Es el punto de partida y la referencia principal para todo lector o usuario
interesado en nuestro trabajo, y por lo tanto deben
considerarse de importancia vital, y no un simple complemento.

Una herramienta útil para escribir archivos agradables y efectivos de una 
forma simple es usando **markdown**, el cual es compatible con muchas
plataformas y permite integrar código al texto. En particular, este tipo de
textos pueden ser intercalados entre los bloques de código en jupyter notebook.
Además, los archivos .md están perfectamente integrados en Github y R-Studio,
haciéndolos muy convenientes para los archivos readme y para hacer la
presentación de nuestros resultados en un ambiente integrado.

Las siguientes referencias proporcionan un buen punto de partida para
trabajar con markdown:

#### Tutoriales de markdown y quick references:
* https://www.markdowntutorial.com/
* https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
* https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf

#### Buenos ejemplos de readme files:
* https://github.com/matiassingers/awesome-readme


# Ejemplo

## Titulos
### Subtitulos
#### and
##### so
###### on ....

## Emphasis

_italics_, **bold**, **_bold italics_**, and Strikethrough: ~~Scratch this~~

## Lists

1. First ordered list item
2. Another item
   * Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
   1. Ordered sub-list
   2. Second nested element
8. And another item.

## Links

[Ir al repositorio](https://github.com/juan-pineda/Modelado-1)

[El mismo pero con nombre](https://github.com/juan-pineda/Modelado-1 "Repositorio de modelado 1")

## Code
Usamos la tilde invertida para incluir líneas de código  
`import numpy as np`  

Usando tres veces la tilde podemos enmarcar bloques de código:
```
a = np.array([1,2,3,4,5])
b = a**2
b.sum()
```
