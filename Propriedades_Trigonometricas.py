#Retorna as propriedades trigonométricas de um ângulo usando a biblioteca math

import math

print("Calcule o radiano, seno, cosseno e tangente de um ângulo")
sucesso = False
while sucesso == False:
    try:    
        angulo = float(input("digite um valor em grau \n"))         

        print("Radiano: ", math.radians(angulo))
        print("Seno: ", math.sin(angulo), "\nCosseno: ", math.cos(angulo), "\nTangente: ", math.tan(angulo)) 
        sucesso = True
    except:
        print("Caractere(s) inválido(s)")
        sucesso = False