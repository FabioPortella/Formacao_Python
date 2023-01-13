from colorama import Fore, Style

# função para desenhar uma árvore de Natal
def desenhar_arvore(altura):
  # desenhar a base da árvore
  for i in range(altura):
    print(" " * (altura - i - 1) + "*" * (2 * i + 1))
  
  # desenhar a raiz da árvore
  print(" " * (altura - 1) + "*")
  print('' + Style.RESET_ALL)
# chamar a função para desenhar uma árvore de altura 5
print(Fore.RED + '')
desenhar_arvore(10)

x = input('Somente uma parada para verificação do código:')
