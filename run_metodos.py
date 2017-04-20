#!/usr/bin/python
# -*- coding: utf-8 -*-

from funciones import *
from metodos import *
import time
import threading


def main():
	op = " "

	while op == " ":
		print"------------------------------------------"
		print("\t\tMetodos de Ordenamiento\t\t")
		print "********************************************"
		print("(1). Ordenamiento por inserción Directa")
		print("(2). Ordenamiento por inserción Binaria")
		print("(3). Ordenamiento por mezcla ")
		print("(4). Ordenamiento por montones(head sort)")
		print("(5). Ordenamiento rápido(quicksort)")
		print("(6). Ordenamiento por conteo(couting sort)")
		print("(7). Ordenamiento por radix sort")
		print("(8). Salir")
		op = raw_input("Selecione Metodo Ordenamiento : ")

		if op != "8":
			op_1 = " "
		else:
			op_1 = "1"

		while op_1 == " ":
			print"------------------------------------------"
			print("\t\tCantidad Datos a Ordenar\t\t")
			print "********************************************"
			print("(1). 1 Millon de Datos")
			print("(2). 2 Millones de Datos")
			print("(3). 5 Millones de Datos ")
			print("(4). 10 Millones de Datos")
			print("(5). 20 Millones de Datos")
			print("(6). Salir")
			op_1 = raw_input("Selecione Cantida Datos : ")
			print '\n'
			op_1= datos(op_1)

		if op == "1":
			print "Has pulsado la opcion."
			print("**Ordenamiento por inserción Directa**")
			print("**Cantidad de Datos a Ordenar "+str(op_1)+"**" '\n')
			tiempo_inicial = time.time()
			lista = llenarLista(op_1)
			nombre = nombreArchivo()
			crearCsv(lista, nombre)
			print("\t\t\t\t\t\t\t\t *****************Lista Desordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista)
			lista_ordenada = lista
			tam = longitud(lista)
			insercionDirecta(lista_ordenada, tam)
			tiempo_inicial_hilo = time.time()
			hilo = threading.Thread(target=insercionDirecta, args=(lista_ordenada, tam))
			hilo.start()
			hilo.join()
			print("\t\t\t\t\t\t\t\t *****************Lista Ordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista_ordenada)
			nombre_final = nombreArchivo()
			crearCsv(lista_ordenada, nombre_final)
			tiempo_final = time.time() - tiempo_inicial
			tiempo_final_hilo = time.time() - tiempo_inicial_hilo
			print ("****Tiempo Espera Sin Hilos****")
			imprimirTiempo(tiempo_final)
			print ("****Tiempo Espera Con Hilos****")
			imprimirTiempo(tiempo_final_hilo)


		elif op == "2":
			print "Has pulsado la opcion."
			print("**Ordenamiento por inserción Binaria**")
			print("**Cantidad de Datos a Ordenar " + str(op_1) + "**"'\n')
			tiempo_inicial = time.time()
			lista = llenarLista(op_1)
			nombre = nombreArchivo()
			crearCsv(lista, nombre)
			print("\t\t\t\t\t\t\t\t *****************Lista Desordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista)
			lista_ordenada = lista
			tam = longitud(lista)
			insercionBinaria(lista_ordenada, tam)
			tiempo_inicial_hilo = time.time()
			hilo = threading.Thread(target=insercionBinaria, args=(lista_ordenada, tam))
			hilo.start()
			hilo.join()
			print("\t\t\t\t\t\t\t\t *****************Lista Ordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista_ordenada)
			nombre_final = nombreArchivo()
			crearCsv(lista_ordenada, nombre_final)
			tiempo_final = time.time() - tiempo_inicial
			tiempo_final_hilo = time.time() - tiempo_inicial_hilo
			print ("****Tiempo Espera Sin Hilos****")
			imprimirTiempo(tiempo_final)
			print ("****Tiempo Espera Con Hilos****")
			imprimirTiempo(tiempo_final_hilo)

		elif op == "3":
			print "Has pulsado la opcion"
			print("**Ordenamiento por mezcla**")
			print("**Cantidad de Datos a Ordenar " + str(op_1) + "**"'\n')
			tiempo_inicial = time.time()
			lista = llenarLista(op_1)
			nombre = nombreArchivo()
			crearCsv(lista, nombre)
			print("\t\t\t\t\t\t\t\t *****************Lista Desordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista)
			mergeSort(lista)
			tiempo_inicial_hilo = time.time()
			hilo = threading.Thread(target=mergeSort, args=(lista))
			hilo.start()
			hilo.join()
			print("\t\t\t\t\t\t\t\t *****************Lista Ordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista)
			nombre_final = nombreArchivo()
			crearCsv(lista, nombre_final)
			tiempo_final = time.time() - tiempo_inicial
			tiempo_final_hilo = time.time() - tiempo_inicial_hilo
			print ("****Tiempo Espera Sin Hilos****")
			imprimirTiempo(tiempo_final)
			print ("****Tiempo Espera Con Hilos****")
			imprimirTiempo(tiempo_final_hilo)

		elif op == "4":
			print "Has pulsado la opcion"
			print("**Ordenamiento por montones(head sort)**")
			print("**Cantidad de Datos a Ordenar " + str(op_1) + "**"'\n')
			tiempo_inicial = time.time()
			lista = llenarLista(op_1)
			nombre = nombreArchivo()
			crearCsv(lista, nombre)
			print("\t\t\t\t\t\t\t\t *****************Lista Desordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista)
			lista_ordenada = lista
			heapsort(lista_ordenada)
			tiempo_inicial_hilo = time.time()
			hilo = threading.Thread(target=heapsort, args=(lista_ordenada))
			hilo.start()
			hilo.join()
			print("\t\t\t\t\t\t\t\t *****************Lista Ordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista_ordenada)
			nombre_final = nombreArchivo()
			crearCsv(lista_ordenada, nombre_final)
			tiempo_final = time.time() - tiempo_inicial
			tiempo_final_hilo = time.time() - tiempo_inicial_hilo
			print ("****Tiempo Espera Sin Hilos****")
			imprimirTiempo(tiempo_final)
			print ("****Tiempo Espera Con Hilos****")
			imprimirTiempo(tiempo_final_hilo)

		elif op == "5":
			print "Has pulsado la opcion"
			print("**Ordenamiento rápido(quicksort)**")
			print("**Cantidad de Datos a Ordenar " + str(op_1) + "**"'\n')
			tiempo_inicial = time.time()
			lista = llenarLista(op_1)
			nombre = nombreArchivo()
			crearCsv(lista, nombre)
			print("\t\t\t\t\t\t\t\t *****************Lista Desordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista)
			lista_ordenada = lista
			quickSort(lista_ordenada)
			tiempo_inicial_hilo = time.time()
			hilo = threading.Thread(target=quickSort, args=(lista_ordenada))
			hilo.start()
			hilo.join()
			print("\t\t\t\t\t\t\t\t *****************Lista Ordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista_ordenada)
			nombre_final = nombreArchivo()
			crearCsv(lista_ordenada, nombre_final)
			tiempo_final = time.time() - tiempo_inicial
			tiempo_final_hilo = time.time() - tiempo_inicial_hilo
			print ("****Tiempo Espera Sin Hilos****")
			imprimirTiempo(tiempo_final)
			print ("****Tiempo Espera Con Hilos****")
			imprimirTiempo(tiempo_final_hilo)

		elif op == "6":
			print "Has pulsado la opcion"
			print("**Ordenamiento por conteo(couting sort)**")
			print("**Cantidad de Datos a Ordenar " + str(op_1) + "**"'\n')
			tiempo_inicial = time.time()
			lista = llenarLista(op_1)
			nombre = nombreArchivo()
			crearCsv(lista, nombre)
			print("\t\t\t\t\t\t\t\t *****************Lista Desordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista)
			lista_ordenada =lista
			a=max(lista)
			counting_sort(lista_ordenada, a)
			tiempo_inicial_hilo = time.time()
			hilo = threading.Thread(target=counting_sort, args=(lista_ordenada, a))
			hilo.start()
			hilo.join()
			print("\t\t\t\t\t\t\t\t *****************Lista Ordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista_ordenada)
			nombre_final = nombreArchivo()
			crearCsv(lista_ordenada, nombre_final)
			tiempo_final = time.time() - tiempo_inicial
			tiempo_final_hilo = time.time() - tiempo_inicial_hilo
			print ("****Tiempo Espera Sin Hilos****")
			imprimirTiempo(tiempo_final)
			print ("****Tiempo Espera Con Hilos****")
			imprimirTiempo(tiempo_final_hilo)

		elif op == "7":
			print "Has pulsado la opcion"
			print("**Ordenamiento por radix sort**")
			print("**Cantidad de Datos a Ordenar " + str(op_1) + "**"'\n')
			tiempo_inicial = time.time()
			lista = llenarLista(op_1)
			nombre = nombreArchivo()
			crearCsv(lista, nombre)
			print("\t\t\t\t\t\t\t\t *****************Lista Desordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista)
			lista_ordenada=radix_sort(lista)
			tiempo_inicial_hilo = time.time()
			hilo = threading.Thread(target=radix_sort, args=(lista))
			hilo.start()
			hilo.join()
			print("\t\t\t\t\t\t\t\t *****************Lista Ordenada***************** \t\t\t\t\t\t\t\t")
			imprimirLista(lista_ordenada)
			nombre_final = nombreArchivo()
			crearCsv(lista_ordenada, nombre_final)
			tiempo_final = time.time() - tiempo_inicial
			tiempo_final_hilo = time.time() - tiempo_inicial_hilo
			print ("****Tiempo Espera Sin Hilos****")
			imprimirTiempo(tiempo_final)
			print ("****Tiempo Espera Con Hilos****")
			imprimirTiempo(tiempo_final_hilo)

		elif op == "8":

			print "Gracias por utilizar nuestro servicio de Metodos de Ordenamiento"
			exit()
		else:
			print("Opcion invalida \n")

		raw_input("Presione Enter para volver al menu ")
		op = " "


if __name__ == '__main__':
	main()