def permutacoes(string, inicio, fim):
    if inicio == fim:
        print("".join(string))
        return

    for i in range(inicio, fim + 1):

        # Faz uma escolha
        string[inicio], string[i] = string[i], string[inicio]

        # Resolve recursivamente o restante
        permutacoes(string, inicio + 1, fim)

        # Desfaz a escolha
        string[inicio], string[i] = string[i], string[inicio]


string = list("ABC")

permutacoes(string, 0, len(string) - 1)
