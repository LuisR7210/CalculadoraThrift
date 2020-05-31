Calculadora Básica


Ejemplo Cliente-Servidor con Thrift 0.13 en Ubuntu 20.04
Cliente en Python3
Servidor en Java

Para ejecutar el programa Calculadora Básica en dos contenedores de docker:
(Nota: primero ejecutar las instrucciones del servidor. Las instrucciones de docker run se deben ejecutar en diferentes terminales.)

Instrucciones para correr el servidor en PowerShell:
1. >docker network create red-cliente-servidor
2. >docker build -t servidor:1.0 "aqui poner ruta completa del Dockerfile del servidor"
3. >docker run --network-alias server --network red-cliente-servidor -it servidor:1.0

Instrucciones para correr el cliente en PowerShell:
1. >docker build -t cliente:1.0 "aqui poner ruta completa del Dockerfile del cliente"
2. >docker run --network red-cliente-servidor -it cliente:1.0


LRHH
