letra = 's'

while letra == 's':

    n1 = input("Digite a primeira nota: ")
    n1 = float(n1)
    n2 = input("Digite a segunda nota: ")
    n2 = float(n2)
    n3 = input("Digite a terceira nota: ")
    n3 = float(n3)

    soma = n1 + n2 + n3
    media = (soma / 3)

    print(f"a media é: {round(media, 2)}")

    if media >= 7:
        print ("Aprovado")
    elif media >= 3:
        print ("recuperação")
    else:
        print ("Reprovado")

    letra = input("deseja lançar uma nova nota [s/n]")