peso = float(input('Digite seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)

print(f'O IMC dessa pessoa é: {round(imc,2)}')
if imc >= 30:
    print('cuidado com sua saude')
else:
    print("tudo ok")
              