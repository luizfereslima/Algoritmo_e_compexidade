def mdc(a, b, acumulador=None):
    # Inicialização do acumulador na primeira chamada
    if acumulador is None:
        acumulador = a if b == 0 else b

    # Caso base: quando b é zero, retorna o acumulador
    if b == 0:
        return acumulador

    # Chamada recursiva em cauda: atualiza os valores de a, b e o acumulador
    return mdc(b, a % b, b)

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

def calculadora():
    while True:
        print("Opções:")
        print("Digite 'somar' para somar dois números")
        print("Digite 'subtrair' para subtrair dois números")
        print("Digite 'multiplicar' para multiplicar dois números")
        print("Digite 'dividir' para dividir dois números")
        print("Digite 'mdc' para encontrar o máximo divisor comum de dois números")
        print("Digite 'sair' para encerrar o programa")
        
        entrada_usuario = input(": ")
        
        if entrada_usuario == "sair":
            break
        elif entrada_usuario in ("somar", "subtrair", "multiplicar", "dividir", "mdc"):
            try:
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, insira valores numéricos.")
                continue

            if entrada_usuario == "somar":
                print("Resultado: ", somar(num1, num2))
            elif entrada_usuario == "subtrair":
                print("Resultado: ", subtrair(num1, num2))
            elif entrada_usuario == "multiplicar":
                print("Resultado: ", multiplicar(num1, num2))
            elif entrada_usuario == "dividir":
                try:
                    print("Resultado: ", dividir(num1, num2))
                except ValueError as e:
                    print(e)
            elif entrada_usuario == "mdc":
                print("Resultado: ", mdc(num1, num2))
        else:
            print("Entrada desconhecida")

# Executa a calculadora
calculadora()
