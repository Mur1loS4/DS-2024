letra = 's'
while letra == 's':


    valor = float(input('Digite o valor para calcular: '))
    porcentagem = float(input('Digite o valor da porcentagem: '))

    soma = valor * porcentagem/100

    print(f'o resultado da porcentagem é: {round(porcentagem, 2)}%')

    letra = input('deseja fazer um novo lanlamento [S/N]:')