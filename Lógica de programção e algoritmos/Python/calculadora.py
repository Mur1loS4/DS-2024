letra ='s'

while letra == 's':

    v1 = float(input('Digite o primeiro valor: '))
    v2 = float(input('Digite o segundo valor: '))

    print('[1] = adição')
    print('[2] = subtração')
    print('[3] = multiplicação')
    print('[4] = divisão')

    v3 = str(input('Digite a qual operação deseja calcular:'))

    if v3 == '1':
        print(v1+v2)
    elif v3 == '2':
        print(v1-v2)
    elif v3 == '3':
        print(v1*v2)
    elif v3 == '4':
        print(v1/v2)

    letra = input('deseja realizar um novo calculo? [s/n]: ')