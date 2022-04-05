# Capa_Fisica

Integrantes:
---Leandro Hernandez C-312
---Lidier Robaina C-313

Este proyecto consiste en simular la Capa Fisica.

Tenemos un conjunto de dispositivos que tienen la siguiente funcionalidad

Computadora: Permite transmitir y recibir informacion a traves de su puerto.

Hub: Recibe informacion por uno de sus puertos y la transmite por los restantes.

Para comunicar varios dispositivos se utiliza un cable.

En dicho cable pueden existir colisiones si se intenta escribir por sus dos extremos a la vez

=======Instrucciones======
<time> create host <name>
<time> create hub <name> <number_of_ports>
<time> connect <port1> <port2>
<time> send <port> <data>
<time> disconnect <port>
