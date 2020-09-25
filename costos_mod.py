class Costos():
	
	def __init__(self, archivo):
		self.archivo = open(archivo,'r')

	def calcula_costo(self, iva = 0):
		suma_costo = 0
		self.archivo.seek(0)
		print("cantidad de datos: ", len(self.archivo.readlines()))
		self.archivo.seek(0)

		for linea in self.archivo.readlines():
			costo = int(linea)
			costo_con_iva = costo + (costo * iva)
			if( costo_con_iva < 25):		
				suma_costo += costo_con_iva
		return suma_costo

	def __del__(self):
		self.archivo.close()
		
	
obj = Costos("costos.txt")	

print("Monto a invertir: ${}".format(obj.calcula_costo()))
print("Monto a invertir (iva): ${:.2f}".format(obj.calcula_costo(0.13)))
