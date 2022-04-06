=======Configuracion=======
La configuracion se encuentra en el archivo config.txt
Hasta ahora solo hay dos formas de configurar.
signal_time=<time> #cada que tiempo quiere que cada dispositivo envie cada bit. Por defecto 10 milisegundos
exit_time=<time> #detiene el timer del sistema y la escritura en la salida cuando pase ese tiempo por defecto a los 2 segundos
Nota: No puede haber espacios en blanco antes y despues del =


======Funcionamiento======

En el archivo main.py se lee cada instruccion.

Antes de ejecutar cada instruccion se espera el <time> de la instruccion y luego se ejecuta la misma.

El proceso anterior se realiza de manera concurrente.

Lo anterior garantiza acercarse al funcionamiento real de una red de computadoras solo en la capa fisica.

Nota: No se considero que el envio fuera a la velocidad de la luz, o sea, instantaneo. Para instrucciones de igual <time>, un sistema perfecto ejecutaria las dos instrucciones al mismo instante de tiempo, este no es el caso, la primera instruccion en el codigo se comenzara a ejecutar mas rapido que instrucciones de igual time solo por estar primero. Le pedimos disculpas a los profesores por este error de interpretacion del problema, creo que a unas horas de la entrega no se puede cumplir 100% con la funcionalidad requerida.

Nuestro proyecto permite collisiones; o sea; que si una computadora quiere transmitir a traves de un puerto y esta recibiendo informacion de otro dispositivo por ese mismo puerto entonces se detectan una collision, es escrito en el fichero correspondiente lo que se ha detectado, acto seguido se esperan 5 milisegundos y se vuelve a intentar enviar la informacion.

Se garantiza que toda la informacion llega a su destino. Pueden existir algunas incongruencias sobre todo con el fichero de salida de los hub, ya que estamos en presencia de procesos concurrentes que se pueden estar ejecutando cada pocos milisegundos y la escritura en el fichero de salida puede hacerse en un orden que aparentemente no debe ser correcto debido al error expuesto con anterioridad(o sea, el error de interpretacion del problema).

