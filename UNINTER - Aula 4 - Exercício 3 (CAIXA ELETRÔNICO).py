''' Escreva um algoritmo que leia um valor e que imprima a quantidade de cédulas
necessárias para pagar esse mesmo valor. Para simplificar, vamos trabalhar apenas
com valores inteiros e com cédulas de R$100, R$50, R$20, R$10, R$5, R$1.'''

print('\033[1;36m='*10 + ' CAIXA ELETRÔNICO ' + '='*10 + '\033[m')

var_valor = int(input('Qual o valor do saque? R$ '))
print(f'Para o valor de R${var_valor:.2f}, serão impressas:')

while True: # Nesse caso, o "while True" está sendo usado só para poder usar o break e, assim, evitar que o programa verifique o que vem depois desnecessariamente.
    if var_valor >= 100:
        var_100 = var_valor // 100
        var_valor = var_valor - (var_100 * 100)
        print(f'{var_100} cédula(s) de R$100,00')
        if not var_valor: # Ou seja, "if var_valor:" significa -> se o "var_valor" existir (tiver alguma coisa nele) faça  (o que está abaixo). Só que, com o "not", se o "var_valor" for zero (não existir [falso]), daí ele faz o que estiver abaixo.
            break

    if var_valor >= 50:
        var_50 = var_valor // 50
        var_valor = var_valor - (var_50 * 50)
        print(f'{var_50} cédula(s) de R$50,00')
        if not var_valor:
            break

    if var_valor >= 20:
        var_20 = var_valor // 20
        var_valor = var_valor - (var_20 * 20)
        print(f'{var_20} cédula(s) de R$20,00')
        if not var_valor:
            break

    if var_valor >= 10:
        var_10 = var_valor // 10
        var_valor = var_valor - (var_10 * 10)
        print(f'{var_10} cédula(s) de R$10,00')
        if not var_valor:
            break

    if var_valor >= 5:
        var_5 = var_valor // 5
        var_valor = var_valor - (var_5 * 5)
        print(f'{var_5} cédula(s) de R$5,00')
        if not var_valor:
            break

    if var_valor >= 1:
        var_1 = var_valor // 1
        var_valor = var_valor - (var_1 * 1)
        print(f'{var_1} cédulas de R$1,00')
        break








