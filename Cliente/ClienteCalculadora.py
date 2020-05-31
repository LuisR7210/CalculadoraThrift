#!/usr/bin/env python

import sys
sys.path.append("gen-py")

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from ThriftCalculadora import CalculadoraBasica

transporte = TSocket.TSocket("server", 8080)
transporte = TTransport.TBufferedTransport(transporte)
protocolo = TBinaryProtocol.TBinaryProtocol(transporte)
cliente = CalculadoraBasica.Client(protocolo)

def switch(operacion, a, b):
   	sw = {
      1: suma(a, b),
      2: resta(a, b),
      3: multiplicacion(a, b),
      4: division(a, b),
   	}
   	return sw.get(operacion, default())

def suma(a, b):
	return cliente.Sumar(a,b)
def resta(a, b):
	return cliente.Restar(a,b)
def multiplicacion(a, b):
	return cliente.Multiplicar(a,b)
def division(a, b):
	resultado = cliente.Dividir(a,b)
	if resultado == -1:
		return "Error: No se puede dividir entre cero..."
	else:
		return resultado
def default():
	return "Opcion Invalida"


transporte.open()
continuar = "s";
while continuar != "0":
	print ("\n------Calculadora Basica------")
	while True:
		try:
			numeroA = int(input("Ingresa el primer número: "))
			numeroB = int(input("Ingresa el segundo número: "))
			print ("\nDime la operación a realizar: ")
			print ("Sumar: Escribe 1")
			print ("Restar: Escribe 2")
			print ("Multiplicar: Escribe 3")
			print ("Dividir: Escribe 4")
			operacion = int(input())
			break
		except:
			print("Solo puedes escribir numeros enteros")
	try:
		print("El resultado es: " + str(switch(operacion, numeroA, numeroB)))
	except:
		print("Error al conectar con el servidor")
	continuar = input("¿Deseas salir? Si(0)")
transporte.close()