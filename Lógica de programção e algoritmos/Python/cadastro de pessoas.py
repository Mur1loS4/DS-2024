from click import clear

def adicionar_pessoa():
    nome = input('Digite seu nome: ')
    email = input('Digite seu e-mail: ')

    with open('pessoa.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{email}\n')

    print('Pessoa cadastrada com sucesso!!!!!')

def listar_pessoa():
    with open('pessoa.txt', 'r') as arquivo:
        print('pessoas cadastradas: ')
        for linha in arquivo:
            nome, email = linha.strip().split(',')
            print(f'Nome: {nome},E-mail: {email}\n')

listar_pessoa()