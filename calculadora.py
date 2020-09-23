class Calculadora():
	
	def __init__(self, num1, num2):		
		self.num1 = num1
		self.num2 = num2

	
	def suma(self):
		return self.num1 + self.num2
    
	def resta(self):
		return self.num1 - self.num2
    
	def multiplicacion(self):
		return self.num1 * self.num2
    
	def division(self):
		try:
		    return self.num1 / self.num2
		except ArithmeticError as e:
			print("Error: Division entre 0")
					

n1 = eval(input("ingrese el primer numero: "))
n2 = eval(input("ingrese el segundo numero: "))

calc = Calculadora(n1, n2)

suma = calc.suma()
resta = calc.resta()
multiplicacion = calc.multiplicacion()
division = calc.division()

print("La suma de {} + {} es: {}".format(n1, n2, suma))
print("La resta de {} - {} es: {}".format(n1, n2, resta))
print("La multiplicacion de {} * {} es: {}".format(n1, n2, multiplicacion))
print("La division de {} / {} es: {}".format(n1, n2, division))