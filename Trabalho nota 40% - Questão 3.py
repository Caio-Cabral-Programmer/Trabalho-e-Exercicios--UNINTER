def funcao_escolha_tipo():
    print('Toras de madeira que estão a venda:')
    print(f'{"PIN - Tora de Pinho":<25} R$150.40')
    print(f'{"PER - Tora de Peroba":<25} R$170.20')
    print(f'{"MOG - Tora de Mogno":<25} R$190.90')
    print(f'{"IPE - Tora de Ipê":<25} R$210.10')
    print(f'{"IMB - Tora de Imbuia":<25} R$220.70')
    while True:
        valor_tora = 0
        tora_tipo = input('Digite o tipo de tora de madeira desejado: [PIN/PER/MOG/IPE/IMB] ').strip().upper()  # Strip e upper, para garantir que os espaços e as letras minúsculas não irão atrapalhar o andamento do programa.
        if tora_tipo == 'PIN':
            valor_tora = 150.40
            break
        elif tora_tipo == 'PER':
            valor_tora = 170.20
            break
        elif tora_tipo == 'MOG':
            valor_tora = 190.90
            break
        elif tora_tipo == 'IPE':
            valor_tora = 210.10
            break
        elif tora_tipo == 'IMB':
            valor_tora = 220.70
            break
        else:
            print('\033[1;31mResposta inválida! Tente novamente.\033[m')  # Mensagem de erro de escrita, colorida em vermelho.
            continue

    return valor_tora

def funcao_qtd_toras():
    while True:
        try:
            desconto = 0
            qtd_toras = int(input('Quantas toras (em m³) você deseja? '))
            if 0 < qtd_toras < 100: # Se alguma destas condições acontecer, será dado o break e pulado o loop.
                desconto = 1
                break
            elif 100 <= qtd_toras < 500:
                desconto = 0.96
                break
            elif 500 <= qtd_toras < 1000:
                desconto = 0.91
                break
            elif 1000 <= qtd_toras <= 2000:
                desconto = 0.84
                break
            elif qtd_toras > 2000: # Se esta condição acontecer, será dado o print abaixo e retornado a início do loop.
                print('\033[1;31mResposta inválida! Não aceitamos pedidos de tora acima de 2000m³.\033[m')
                continue
            else:
                print('\033[1;31mResposta inválida! Tente novamente.\033[m')
                continue

        except ValueError: # Caso a resposta seja um valor inválido, acionará este except e voltará ao loop.
            print('\033[1;31mResposta inválida! Escreva um número válido.\033[m')

    print()
    return qtd_toras, desconto # Retorno de dois valores.

def funcao_transporte():
    print('Tipos de transporte:')
    print('1 - Transporte Rodoviário  - R$1000.00')
    print('2 - Transporte Ferroviário - R$2000.00')
    print('3 - Transporte Hidroviário - R$2500.00')

    while True:
        valor_transporte = 0
        transporte = int(input('Qual transporte você escolhe? [1/2/3] '))
        if transporte == 1:
            valor_transporte = 1000
            break
        elif transporte == 2:
            valor_transporte = 2000
            break
        elif transporte == 3:
            valor_transporte = 2500
            break
        else:
            print('\033[1;31mResposta inválida! Escreva um número válido.\033[m')
            continue

    return valor_transporte

# Programa Principal

print('=' * 10 + ' Sistema desenvolvido por Caio Fellipe Bezerra Cabral ' + '=' * 10)
print('\033[7;39m=-'*10 + ' MADEIREIRA UNINTER FRESH WOOD ' + '-='*10 + '\033[m')

var_valor_tora = funcao_escolha_tipo()
var_qtd_toras, var_desconto = funcao_qtd_toras()
var_valor_transporte = funcao_transporte()
var_valor_total = ((var_valor_tora * var_qtd_toras) * var_desconto) + var_valor_transporte

# Saída com o resultado final:
print()
print(f'\033[1;32mValor total a ser pago: R${var_valor_total:.2f}.\033[m') # Resultado final destacado em verde.



