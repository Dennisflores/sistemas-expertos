import numpy as np
from time import time

catalogo_libros = np.loadtxt('catalogo_libros.txt')
libros_24_meses = np.loadtxt('libros_24_meses.txt')

inicio = time()

libros_vendidos = np.intersect1d(catalogo_libros, libros_24_meses,assume_unique=True)

tiempo_transcurrido = time() - inicio

print("{} segs".format(tiempo_transcurrido))
print("libros vendidos:", len(libros_vendidos))

# assume_unique = true
# Si es True, se supone que las matrices de entrada son únicas, lo que puede acelerar el cálculo. 
# Si Verdadero pero ar1 o ar2 no son únicos, pueden producirse resultados incorrectos e índices fuera 
# de límites. El valor predeterminado es falso.