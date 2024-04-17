def somaAuxiliar(vetor, indice, resultado):
    """
    Função auxiliar para calcular a soma dos elementos de uma lista de forma recursiva em cauda.
    """
    if indice == len(vetor):
        return resultado
    return somaAuxiliar(vetor, indice + 1, resultado + vetor[indice])  # Chamada recursiva em cauda

def somaVetor(vetor):
    """
    Função principal para calcular a soma dos elementos de uma lista.
    """
    return somaAuxiliar(vetor, 0, 0)

# Exemplo de uso
vetor = [1, 2, 3, 4, 5]
print("A soma dos elementos da lista é:", somaVetor(vetor))
