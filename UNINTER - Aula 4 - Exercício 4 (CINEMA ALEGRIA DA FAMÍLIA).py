''' Um cinema cobra preços diferentes para os ingressos, de acordo com a idade da pessoa.
Se a pessoa tiver menos de 3 anos de idade, o ingresso será gratuito; tiver entre 3 e 12 anos,
o ingresso custará R$15; se tiver mais de 12 anos, custará R$30.
- Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes o preço
do ingresso do cinema;
- Encerre o laço, usando um break quando o usuário digitar zero;
- Após encerrar o laço, apresente na tela o total de pessoas que compraram ingressos, o
total de dinheiro arrecadado e a média de idade das pessoas.
'''

var_total_pessoas = 0
var_total_dinheiro = 0
var_idade_soma = 0
var_media_idade = 0

print('\033[1;36m=-'*10 + ' CINEMA ALEGRIA DA FAMÍLIA ' + '-='*10 + '\033[m')
print('\033[1;32m') # Adicionando cor à sequência de print abaixo.
print('GRATUITO - Para menores de 3 anos.')
print('R$15.00 - Para crianças entre 3 e 12 anos.')
print('R$30.00 - Para maiores de 12 anos.')
print('\033[m') # Encerrando as cores acima aqui.

while True:
    print('[Digite "0" (zero) para encerrar sua compra ou continue comprando]')
    var_idade = int(input('Qual sua idade? '))
    if var_idade == 0:
        break
    elif var_idade < 3:
        print('Valor do ingresso: GRATUITO')
        var_total_pessoas += 1
        var_idade_soma += var_idade
        continue
    elif 3 <= var_idade <= 12:
        var_total_pessoas += 1
        var_total_dinheiro += 15
        var_idade_soma += var_idade
        print('Valor do ingresso: R$15.00')
    else:
        var_total_pessoas += 1
        var_total_dinheiro += 30
        var_idade_soma += var_idade
        print('Valor do ingresso: R$30.00')

if var_total_pessoas > 0:
    var_media_idade = var_idade_soma / var_total_pessoas

    print(f'{var_total_pessoas} pessoas compraram os ingressos.')
    print(f'R${var_total_dinheiro:.2f} foram arrecadados.')
    print(f'Média de idade: {var_media_idade} anos.')
else: print('PROGRAMA ENCERRADO.')



