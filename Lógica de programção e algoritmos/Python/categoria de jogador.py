inf = int(input('Informe sua idade: '))

if inf <= 13:
    print('Categoria infanti')
elif inf <= 17:
    print('Categoria juvenil')
else:
    print('Categoria senior')