def hanoi_3(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return

    hanoi_3(n - 1, origem, auxiliar, destino)

    print(f"Mover disco {n} de {origem} para {destino}")

    hanoi_3(n - 1, auxiliar, destino, origem)


def hanoi_4(n, origem, destino, auxiliar1, auxiliar2):
    if n == 0:
        return

    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return

    k = n // 2

    # Move k discos usando os 4 pinos
    hanoi_4(k, origem, auxiliar1, destino, auxiliar2)

    # Move os discos restantes usando 3 pinos
    hanoi_3(n - k, origem, destino, auxiliar2)

    # Move os k discos para o destino
    hanoi_4(k, auxiliar1, destino, origem, auxiliar2)


n = 4

hanoi_4(n, "A", "D", "B", "C")
