#Calculadora de fatorial usando o laço while

print("Calculadora de fatorial")

sucesso = False
while sucesso == False:
    try:
        n = int(input("Digite um número: "))
        c = n
        f = 1
        
        if n < 0:           
            n = b 
        #Condição inválida usada apenas para o algoritmo mandar pro except.
        #Posteriormente adicionar um raise aqui no lugar dessa condição. 
        if n == 0:
            f = 1

        while n > 0:
            f *= n
            n -= 1
        
        
        print(f"o fatorial de {c} é {f}")
        sucesso = True
    except:
        print("Caráctere inválido")
        sucesso = False