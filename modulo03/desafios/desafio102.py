# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(num, show=False):
    """Calcula o Fatorial de um número

    Args:
        num (int): O número a ser calculado.
        show (bool, optional): Mostrar ou não o cálculo.

    Returns:
        int: O valor do Fatorial de um número.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

num = int(input("Digite um número: "))
show = str(input("Processo de cálculo será mostrado ou não? (T/F): ")).strip().upper()[0]
if show == "T":
    show = True
else:
    show = False
print(fatorial(num, show=show))

# help(fatorial)