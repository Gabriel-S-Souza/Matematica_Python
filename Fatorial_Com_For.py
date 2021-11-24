# Calculadora de fatorial usando o laço for

try:
	print ("Este algorítmo calcula o fatorial de um número")
	fatorial = 1
	numero = int (input("Digíte um número:"))
	if numero > 0:
		for item in range (1, numero + 1):
			fatorial = fatorial * item
		print (fatorial)
except:
	print ("Digite um numero inteiro")