#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import csv


def imprimirLista(lista):
	print lista

def llenarLista(limite):
	lista = []
	for i in range(0, limite):
		lista.append(random.randint(-9999, 9999))
	return lista


def nombreArchivo():
	nombre = raw_input("Ingrese nombre del archivo: ")
	return nombre

def crearCsv(lista, nombre):
	datos = open(nombre + ".csv", "w")
	datos_csv = csv.writer(datos)
	datos_csv.writerow(lista)
	datos.close()

def leerCsv(lista_2, nombre):
	datos = open(nombre + ".csv", "r")
	datos_csv = csv.reader(datos, delimiter = ",")
	for variable in (datos_csv):
		lista_2.append(variable)
	datos.close()
	return lista_2

def longitud(lista):
	return len(lista)

def imprimirTiempo(tiempo_final):
	print ("Proceso finalizado en %0.5f segundos" %tiempo_final)

def datos(opcion):
	if opcion == "1":
		op_1 = 1000000

	if opcion == "2":
		op_1 = 2000000

	if opcion == "3":
		op_1 = 5000000

	if opcion == "4":
		op_1 = 10000000

	if opcion == "5":
		op_1 = 20000000

	return op_1



