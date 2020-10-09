import numpy as np
from time import time

# se generan los datos gran el metodo truncnorm de la libreria scipy
def generarDatos(media, escala, tamanio):
	return np.random.normal(loc = media, scale = escala, size = tamanio)	           

# se calcula la sumatoria de los puntos menores a 500
def sumatoriaPuntos(datos):
	suma = 0
	for dato in datos:
		if(dato < 500): #para el caso se debia trabajar con 500000 pero todos los datos 
		# generados son menores a ese numero dados los datos de la media y la escala por eso se utilizo 
		# 500 para filtrar de mejor manera
			suma += dato
	return suma	

inicio = time()

media = 500
escala = 30
tamanio = 10000000

datos = generarDatos(media, escala, tamanio)
suma = sumatoriaPuntos(datos)
tiempo_transcurrido = time() - inicio

print("Suma de los valores menores a 500: {} ".format(suma))
# print(min(datos)) #para conocer el dato menor generado
# print(max(datos)) #para conocer el dato menor generado
print("\nTiempo transcurrido: {} segs".format(tiempo_transcurrido))