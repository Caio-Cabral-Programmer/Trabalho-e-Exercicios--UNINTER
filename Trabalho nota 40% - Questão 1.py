print('\033[1;36m=-'*10 + ' PLANO DE SAÚDE FULL LIFE ' + '-='*10 + '\033[m')

# EXIGÊNCIA DE CÓDIGO 1 de 6
print('- Sistema desenvolvido por Caio Fellipe Bezerra Cabral -')

# EXIGÊNCIA DE CÓDIGO 2 e 6 de 6
var_valor_base = float(input('Digite o valor base do plano: R$')) # Entrada por teclado do valor base do plano.
var_idade = int(input('Digite a idade do cliente: ')) # Entrada por teclado da idade do cliente.

# EXIGÊNCIA DE CÓDIGO 3, 4, 5 e 6 de 6
if 0 <= var_idade < 19: # Sequência de condições para se obter o valor mensal do plano de acordo com a idade do cliente.
    var_valor_mensal = var_valor_base
elif 19 <= var_idade < 29:
    var_valor_mensal = var_valor_base * 1.5
elif 29 <= var_idade < 39:
    var_valor_mensal = var_valor_base * 2.25
elif 39 <= var_idade < 49:
    var_valor_mensal = var_valor_base * 2.4
elif 49 <= var_idade < 59:
    var_valor_mensal = var_valor_base * 3.5
else: var_valor_mensal = var_valor_base * 6

# Saída com o valor mensal do plano.
print(f'O valor mensal do plano é de R${var_valor_mensal:.2f}.')
