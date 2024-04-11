v1 = int(input('Digite um valor fatorial: '))

def fatorial (v1):
     if v1 < 0:
       return
     else:
      resultado = 1
      for x in range(1, v1 + 1):
        resultado *= x
      return resultado

print(f"O fatorial de {v1} é {fatorial(v1)}")
