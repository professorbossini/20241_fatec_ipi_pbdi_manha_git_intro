import calculadora
def main():
  a = 2
  b = 3
  soma = calculadora.somar(a, b)
  subtracao = calculadora.subtrair(a, b)
  produto = calculadora.multiplicar(a, b)
  print(f'{a} + {b} = {soma}')
  print(f'{a} - {b} = {subtracao}')
  print(f'{a} * {b} = {produto}')

main()