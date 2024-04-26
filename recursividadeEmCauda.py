def somaAuxiliar(vetor, indice, resultado):
    """
    Função auxiliar para calcular a soma dos elementos de uma lista de forma recursiva em cauda. Isso define uma função chamada somaAuxiliar que recebe três parâmetros: vetor, que é a lista de números; indice, que é o índice atual na lista que estamos avaliando; e resultado, que é a soma parcial dos elementos até o momento.
    """
            
    if indice == len(vetor): # Esta linha verifica se o índice atual é igual ao comprimento da lista vetor. Se for igual, significa que chegamos ao final da lista e então retornamos o resultado atual, ou seja, a soma total dos elementos.
        return resultado #Retorna a soma total dos elementos da lista.
    return somaAuxiliar(vetor, indice + 1, resultado + vetor[indice])  # Chamada recursiva em cauda. 
    """
    Se ainda não chegamos ao final da lista, fazemos uma chamada recursiva para a função somaAuxiliar, passando o mesmo vetor, aumentando o índice em 1 para avançar para o próximo elemento, e atualizando o resultado com o valor do elemento atual somado ao resultado parcial.
    """


def somaVetor(vetor): # Aqui, definimos uma função principal chamada somaVetor, que recebe apenas um parâmetro, vetor, a lista que queremos somar.
        
    return somaAuxiliar(vetor, 0, 0) # 
    """
    Para calcular a soma dos elementos da lista, chamamos a função somaAuxiliar com os parâmetros vetor, 0 (o índice inicial) e 0 (a soma parcial inicial).
    """

# Exemplo de uso
vetor = [1, 2, 3, 4, 6]
print("A soma dos elementos da lista é:", somaVetor(vetor))
