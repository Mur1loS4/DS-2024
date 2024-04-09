letra = 's'

while letra == 's':

    v1 = float(input('Digite o valor que deseja transformar em real: '))

    print("Em dolar: $ ", (5*v1))
    print("Em reais: $", (v1 / 5))

    letra = input('Deseja fazer um novo lançamento? [S/N]: ')