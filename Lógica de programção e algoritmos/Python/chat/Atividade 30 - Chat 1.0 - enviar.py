from click import clear
import socket

nome = input("Qual seu nome?")

while True:
    clear()
    mensagem = input("Digite sua mensagem: \n")
    with open(r"\\10.144.227.216\compartilhar", "a") as  arquivo:
        arquivo.write(f"{nome} | {mensagem} \n")