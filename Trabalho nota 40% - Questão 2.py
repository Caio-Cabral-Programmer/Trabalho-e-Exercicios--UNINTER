# Questão 2
def funcao_menu_pizzaria ():
    print('=' * 10 + ' Sistema desenvolvido por Caio Fellipe Bezerra Cabral ' + '=' * 10)
    print('\033[1;33m=' * 25 + ' PIZZARIA ITALIANA PLUS ' + '=' * 25 + '\033[m')
    print('-' * 32 + ' Cardápio ' + '-' * 32)
    print('-' * 74)
    print('---|   Tamanho   |    Pizza Salgada (PS)   |      Pizza Doce (PD)     |---')
    print('---|      P      |          R$30.00        |          R$34.00         |---')
    print('---|      M      |          R$45.00        |          R$48.00         |---')
    print('---|      G      |          R$60.00        |          R$66.00         |---')
    print('-' * 74)

# Programa Principal
funcao_menu_pizzaria() # Print do menu através de uma função. Muito útil para, quando for necessário, colocar o print do menu no loop.
var_valor_total = 0 # Variável acumuladora para somar nela todos os pedidos.
while True:
    var_valor_pedido = 0 # Variável para coletar o valor de cada pedido individualmente.
    var_sabor = input('Qual sabor de pizza você deseja? [PS/PD] ').strip().upper() # Strip e upper, para garantir que os espaços e as letras minúsculas não irão atrapalhar o andamento do programa.
    if var_sabor == 'PS':
        var_tamanho = input('E qual o tamanho? [P/M/G] ').strip().upper()
        if var_tamanho == 'P':
            var_valor_pedido += 30
        elif var_tamanho == 'M':
            var_valor_pedido += 45
        elif var_tamanho == 'G':
            var_valor_pedido += 60
        else:
            print('\033[1;31mTamanho inválido! Tente novamente.\033[m') # Mensagem de erro de escrita, colorida em vermelho.
            print()
            continue

    elif var_sabor == 'PD':
        var_tamanho = input('E qual o tamanho? [P/M/G] ').strip().upper()
        if var_tamanho == 'P':
            var_valor_pedido += 34
        elif var_tamanho == 'M':
            var_valor_pedido += 48
        elif var_tamanho == 'G':
            var_valor_pedido += 66
        else:
            print('\033[1;31mTamanho inválido! Tente novamente.\033[m')
            print()
            continue

    else:
        print('\033[1;31mSabor inválido! Tente novamente.\033[m')
        print()
        continue

    var_valor_total += var_valor_pedido # Variável acumuladora recebendo o valor do atual pedido.

    var_continuar = input('Deseja fazer mais um pedido? [S/N] ').strip().upper()
    print()
    if var_continuar == 'N':
        break

# Saída com o valor total da compra:
print(f'\033[1;32mValor total a ser pago: R${var_valor_total:.2f}.\033[m') # Resultado final destacado em verde.


