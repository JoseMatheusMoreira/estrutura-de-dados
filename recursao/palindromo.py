def palindromo(palavra, inicio, fim):
    if inicio >= fim:
        return True

    if palavra[inicio] != palavra[fim]:
        return False

    return palindromo(palavra, inicio + 1, fim - 1)


palavra = "arara"

if palindromo(palavra, 0, len(palavra) - 1):
    print("É palíndromo")
else:
    print("Não é palíndromo")
