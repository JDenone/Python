import os

while True:
  nome = input("Digite o seu nome: ")
  last_nome = input("Digite seu último nome: ")
  c = 0
  while c < 10:
    print(nome,", você é um desenvolvedor de Qualidade!")
    c += 1
  print(os.name)
  input("Pressione ENTER para continuar!")

  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
