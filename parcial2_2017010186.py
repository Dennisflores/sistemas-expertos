import numpy as np
from time import time

# se generan los datos gran el metodo truncnorm de la libreria scipy
def generarDatos(media, escala, tamanio):
	return np.random.normal(loc = media, scale = escala, size = tamanio)	           

# se calcula la sumatoria de los puntos menores a 500
def sumatoriaPuntos(datos):	
	return sum([valor for valor in datos if valor < 500])
		
inicio = time()

media = 500
escala = 30
tamanio = 10000000

datos = generarDatos(media, escala, tamanio)
suma = sumatoriaPuntos(datos)
tiempo_transcurrido = time() - inicio

print("Suma de los valores menores a 500: {} ".format(suma))
print("\nTiempo transcurrido: {} segs".format(tiempo_transcurrido))