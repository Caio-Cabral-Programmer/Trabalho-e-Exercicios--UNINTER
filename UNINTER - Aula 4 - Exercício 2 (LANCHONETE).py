'''Escreva um algoritmo que mostre, na tela, quatro produtos a serem comprados em uma lanchonete:
- Coxinha - R$5.00
- Pastel - R$7.00
- Café - R$4.00
- Suco - R$6.00
Faça um algoritmo em que você seleciona o produto que quer comprar e a quantidade. Faça isso até
que decida encerrar o programa.
Ao final, mostre o valor final do pedido a ser pago.'''

print('\033[1;33m='*10 + ' LANCHONETE ' + '='*10 + '\033[m')
print(f'1 - {'Coxinha':10} R$5.00 ')
print(f'2 - {'Pastel':10} R$7.00')
print(f'3 - {'Café':10} R$4.00')
print(f'4 - {'Suco':10} R$6.00')
print(f'5 - PEDIDO CONCLUÍDO.')

print('-'*10 + ' PEDIDO ' + '-'*10)

var_coxinha = 0
var_pastel = 0
var_cafe = 0
var_suco = 0

var_pedido = int(input('O que você gostaria [1, 2, 3, 4 ou 5]? '))
while True:
    if var_pedido == 5:
        break
    var_quantidade = int(input('Quantas unidades? '))
    if var_pedido == 1:
        var_coxinha += var_quantidade
    elif var_pedido == 2:
        var_pastel += var_quantidade
    elif var_pedido == 3:
        var_cafe += var_quantidade
    elif var_pedido == 4:
        var_suco += var_quantidade
    var_pedido = int(input('Mais algo [1, 2, 3, 4 ou 5]? '))
    if var_pedido == 5:
        break

var_total = (var_coxinha * 5) + (var_pastel * 7) + (var_cafe * 4) + (var_suco * 6)
if var_total == 0:
    print('- PEDIDO CANCELADO - ')
else:
    print(f'TOTAL A PAGAR: R${var_total:.2f}')


