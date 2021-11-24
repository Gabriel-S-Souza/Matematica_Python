# Calculadora de Fatorial com função recursiva

def fat(n):
    if n < 0:
        print("Use um número inteiro igual ou maior que 0")
        return
    elif n == 0:
        return 1
    else:    
        return n * fat(n - 1)

def initFat():
    n = int(input("Digite um número:\n"))
    f = fat(n)    
    print(str(n) + "!= " + str(f))

initFat()
   
'''Representação escrita da função recursiva usando o n=5:
(5*(5-1*(4-1*(3-1*(2-1*(1-1))))))
5*4*3*2*1*0  (quando n=0 --> n=1)
5*4*3*2*1*1
120
'''