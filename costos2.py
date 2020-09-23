from time import time

sumaCostos = 0
inicio = time()

with open('costos.txt','r') as input:
    for linea in input.readlines():
    	if(int(linea) < 25):
    	    sumaCostos += int(linea) 	 					

tiempo_transcurrido = time() - inicio

print("{} segs".format(tiempo_transcurrido))
print("Monto a invertir: ${}".format(sumaCostos))
