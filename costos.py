from time import time
archivo = open('costos.txt','r')

sumaCostos = 0
inicio = time()

for linea in archivo.readlines():
	if(int(linea) < 25):		
		sumaCostos += int(linea) 

archivo.close()

tiempo_transcurrido = time() - inicio

print("{} segs".format(tiempo_transcurrido))
print("Monto a invertir: ${}".format(sumaCostos))
