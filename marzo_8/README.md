# PRELIMINARES

## Para Instalar Linux Ubuntu:

1. Descargar el instalador apropiado desde
[aquí](https://www.ubuntu.com/download/desktop "Ubuntu's Homepage")

2. Crear un disco de arranque en una memoria USB a apartir del archivo .ISO  
(En ubuntu se hace usando el _Startup disk creator_)

3. Conectar la memoria y encender el computador.

4. Oprimir repetidamente `F2`  en el arranque para entrar a la bios, y seleccionar el disco externo como el de mayor prioridad para “bootear” el equipo. Salvar cambios y salir.

4. En caso de un error que los deje viendo un command window sin iniciar el OS, algunos se pueden burlar dando `TAB` y digitando “live” y luego Enter.

6. Una vez en la sesión _“live”_ en Ubuntu, clicar en el ícono de instalar y seguir las instrucciones.
Es importante tener conexión a internet para hacer de una vez las principales actualizaciones.
(**Ojo a no olvidar su contraseña**, la van a necesitar todo el tiempo!)

7. El instalador va a preguntar si desean eliminar Windows y dejar solo Ubuntu, o si prefieren mantener los dos sistemas operativos (OS). En el segundo caso, les preguntará cuánta de la memoria disponible desean dejar para cada OS.  Aunque en general sale todo bien, es mejor hacer un back up antes de este proceso, pues siempre existe algún riesgo errores en el sistema.

## Install Python on windows via Anaconda (recomendado):

### Tutorial:
https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444

### Descargar Anaconda:
https://www.anaconda.com/download/#windows

Instalar Anaconda usando el archivo ejecutable.
En caso de duda durante la instalación, simplemente mantener las configuraciones por defecto.
Activar la casilla _“Add Anaconda to my PATH environment variable”_

Para testar:
1. Abrir un terminal “Anaconda prompt”.
2. Digitar los siguiente comandos y ver si los reconoce

   ```conda list
   python --version
   jupyter notebook  # Debe abrir un jupyter notebook en el navegador de internet
   where python
   where conda```
   
Si no activaron la casilla para actualizar el PATH, hay que hacerlo manualmente.
Abrir el “command prompt” o el “cmd”, y digitar algo como:

`SETX PATH “%PATH%;C:\...\....;C:\...\...\Anaconda2`

Donde los dos paths sugeridos deben corresponder a las salidas en el “anaconda prompt” de los comandos:   
```where python 
where conda```

Para que el sistema detecte los cambios en PATH hay que cerrar el terminal y abrir uno nuevo, para que el sistema lea de nuevo el archivo de configuraciones.

Python ya debería estar disponible. Para asegurarse, en el “cmd” digitar:
`python`


