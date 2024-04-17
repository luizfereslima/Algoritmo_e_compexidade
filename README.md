# Documentação do Projeto: Soma de Elementos de uma Lista

## Visão Geral

Este projeto consiste em um conjunto de funções em Python para calcular a soma dos elementos de uma lista de forma recursiva em cauda.

## Funcionalidades

O projeto inclui duas funções principais:

1. **Função `somaAuxiliar`**: Esta função é responsável por calcular a soma dos elementos de uma lista de forma recursiva em cauda. Ela é chamada pela função `somaVetor`.

2. **Função `somaVetor`**: Esta função é a função principal do projeto e é responsável por chamar a função `somaAuxiliar` com os parâmetros adequados.

## Uso

Para utilizar este projeto, siga as instruções abaixo:

1. Importe as funções para o seu script Python:

   ```python
   from soma_lista import somaVetor
   ```

2. Crie uma lista de números inteiros.

3. Chame a função `somaVetor` passando a lista como argumento. Esta função retornará a soma dos elementos da lista.

   ```python
   vetor = [1, 2, 3, 4, 5]
   resultado = somaVetor(vetor)
   print("A soma dos elementos da lista é:", resultado)
   ```

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **soma_lista.py**: Este é o arquivo principal do projeto que contém a implementação das funções `somaAuxiliar` e `somaVetor`.

## Requisitos

Este projeto requer Python 3.x para ser executado.

## Autor

Este projeto foi desenvolvido por Luiz Felipe Dias Cardoso Feres Lima.
