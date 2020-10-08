from scipy.stats import truncnorm
from time import time

def generarDatos(media, valorMin, valorMax, escala, tamanio):
	return truncnorm((valorMin - media) / escala, (valorMax - media) / escala, loc=media, scale=escala).rvs(size=tamanio)	           

inicio = time()

media = 500
valorMin = 1
valorMax = 1000000000
escala = 30
tamanio = 10000000
datos = generarDatos(media, valorMin, valorMax, escala, tamanio)
tiempo_transcurrido = time() - inicio

print("Tiempo transcurrido: {} segs".format(tiempo_transcurrido))
print(min(datos))
print(max(datos))