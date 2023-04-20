investimento_mensal = float(input('Informe o valor que será investido por mês: '))
taxa_juros_mensal = float(input('Informe a taxa de juros mensal em decimal: '))
saldo = 0

for mes in range(1, 13):
    saldo += investimento_mensal
    saldo *= (1 + taxa_juros_mensal)
    print(f'Saldo após o mês {mes}: R$ {saldo:.2f}')

continuar = input('Deseja calcular o próximo ano? (S/N) ')

while continuar.upper() == 'S':
    for mes in range(1, 13):
        saldo += investimento_mensal
        saldo *= (1 + taxa_juros_mensal)
    print(f'Saldo após um ano: R$ {saldo:.2f}')
    continuar = input('Deseja calcular o próximo ano? (S/N) ')
    
print('Programa finalizado.')