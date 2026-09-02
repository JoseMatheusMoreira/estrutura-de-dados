def inverter(vetor, inicio, fim):
    if inicio >= fim:
        return

    vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]

    inverter(vetor, inicio + 1, fim - 1)


vetor = [1, 2, 3, 4, 5]

inverter(vetor, 0, len(vetor) - 1)

print(vetor)
