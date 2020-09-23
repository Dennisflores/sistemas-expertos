from time import time
import numpy as np
archivo = np.loadtxt('costos.txt')

sumaCostos = 0
inicio = time()

for linea in archivo:
	if(int(linea) < 25):		
		sumaCostos += int(linea) 

tiempo_transcurrido = time() - inicio

print("{} segs".format(tiempo_transcurrido))
print("Monto a invertir: ${}".format(sumaCostos))