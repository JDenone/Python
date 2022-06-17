def call_numbers(): # def é utilizado sempre que for necessário criar uma função
  for number in range(0,10):
    print(number)

def call_numbers_whit_limit(limit): #limit é o parametro
  list = range(limit) #dentro de range, define qual o limite do range que pode ser definido ou variável
  for number in list[0:limit]: # a lista será impressa conforme o limite definido no chamado da função.
    print(number)

# call_numbers_whit_limit(50) # dentro dos parenteses é definido o limite do contador

# É recomendado utilizar parâmetros nomeados, como no exemplo abaixo

def calculator(x=10, y=15): # dentro dos parênteses estão so parâmetros nomeados
  return x-y # return guarda o valor obtido pela operação de x e y

result = calculator()
print ('Result is ', result)
