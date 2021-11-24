#Calculadora com Python

def adicao(num1, num2):
    resultado = num1 + num2
    return resultado


def subtracao(num1, num2):
    resultado = num1 - num2
    return resultado


def multiplicacao(num1, num2):
    resultado = num1 * num2
    return resultado


def divisao(num1, num2):
    resultado = num1 / num2
    return resultado


def ligar():
    print('Calculadora ligada!\nRealize operações entre dois números!')
    num1 = int(input('Digíte o primeiro número:  '))
    operacao = int(input(
        '\nPara realizar conta de\nMais(+) digite 1\nMenos(-) digite 2\nVezes(*) digite 3\nDividir(/) digite 4\n'))
    num2 = int(input('\nDigíte o segundo número:  '))
    if operacao == 1:
        resultado = adicao(num1, num2)
        print('RESULTADO: ' + str(resultado))

    if operacao == 2:
        resultado = subtracao(num1, num2)
        print('RESULTADO: ' + str(resultado))

    if operacao == 3:
        resultado = multiplicacao(num1, num2)
        print('RESULTADO: ' + str(resultado))

    if operacao == 4:
        resultado = divisao(num1, num2)
        print('RESULTADO: ' + str(resultado))


ligar()
