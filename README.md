# Documentação do Código: Calculadora com Recursividade em Cauda

## Descrição Geral
Este programa implementa uma calculadora que realiza operações aritméticas básicas (soma, subtração, multiplicação, divisão) e calcula o Máximo Divisor Comum (MDC) usando recursividade em cauda. A interface é de linha de comando, onde o usuário pode escolher a operação desejada e fornecer os números de entrada.

## Estrutura do Programa
O programa é composto pelas seguintes funções:

1. `mdc(a, b, acumulador=None)`: Calcula o Máximo Divisor Comum de dois números usando recursividade em cauda.
2. `somar(a, b)`: Retorna a soma de dois números.
3. `subtrair(a, b)`: Retorna a diferença entre dois números.
4. `multiplicar(a, b)`: Retorna o produto de dois números.
5. `dividir(a, b)`: Retorna o quociente da divisão de dois números. Lança um erro se o divisor for zero.
6. `calculadora()`: Função principal que gerencia a interação com o usuário e executa as operações escolhidas.

## Funções

### Função: `mdc`
```python
def mdc(a, b, acumulador=None):
    if acumulador is None:
        acumulador = a if b == 0 else b

    if b == 0:
        return acumulador

    return mdc(b, a % b, b)
```
- **Descrição**: Calcula o Máximo Divisor Comum (MDC) de dois números usando recursividade em cauda.
- **Parâmetros**:
  - `a`: Primeiro número.
  - `b`: Segundo número.
  - `acumulador`: Valor acumulado para a recursão.
- **Retorno**: O MDC de `a` e `b`.

### Função: `somar`
```python
def somar(a, b):
    return a + b
```
- **Descrição**: Retorna a soma de dois números.
- **Parâmetros**:
  - `a`: Primeiro número.
  - `b`: Segundo número.
- **Retorno**: A soma de `a` e `b`.

### Função: `subtrair`
```python
def subtrair(a, b):
    return a - b
```
- **Descrição**: Retorna a diferença entre dois números.
- **Parâmetros**:
  - `a`: Primeiro número.
  - `b`: Segundo número.
- **Retorno**: A diferença entre `a` e `b`.

### Função: `multiplicar`
```python
def multiplicar(a, b):
    return a * b
```
- **Descrição**: Retorna o produto de dois números.
- **Parâmetros**:
  - `a`: Primeiro número.
  - `b`: Segundo número.
- **Retorno**: O produto de `a` e `b`.

### Função: `dividir`
```python
def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b
```
- **Descrição**: Retorna o quociente da divisão de dois números. Lança um erro se o divisor for zero.
- **Parâmetros**:
  - `a`: Primeiro número.
  - `b`: Segundo número.
- **Retorno**: O quociente da divisão de `a` por `b`.

### Função: `calculadora`
```python
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
```
- **Descrição**: Gerencia a interação com o usuário e executa as operações escolhidas.
- **Lógica**:
  - Exibe um menu de opções ao usuário.
  - Lê a entrada do usuário.
  - Executa a operação correspondente com base na escolha do usuário.
  - Continua em loop até que o usuário digite "sair".

### Execução Principal

```python
# Executa a calculadora
calculadora()
```
- **Descrição**: Inicia a execução do programa chamando a função `calculadora`.

## Exemplo de Uso
1. O programa exibe um menu de opções.
2. O usuário escolhe uma operação digitando a palavra correspondente (e.g., "somar").
3. O programa solicita dois números ao usuário.
4. O programa executa a operação escolhida e exibe o resultado.
5. O processo repete até que o usuário digite "sair".
