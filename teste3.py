N = int(input())

while(N > 0):
    entrada = input()
    A, B = entrada.split()
    saida = "encaixa" if A.endswith(B) else "nao encaixa"
    print(saida)
    N -= 1 