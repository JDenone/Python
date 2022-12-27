import getpass

print('****************************************')
print('*** School of Net - Caixa Eletrônico ***')
print('****************************************')

#   o input recebe os dados da iteração e salva como uma string e é necessário ter uma variável para receber 
# os dados da iteração
account_typed = input('Digite sua conta: ')
password_typed = getpass.getpass('Digite sua senha: ')
print(account_typed)
print(password_typed)

accounts_list = {
    '0001-02': {
        'password' : '123456',
        'name' : 'Cliente 1',
        'value' : 0
    },
    '0002-02' : {
        'password' : '456123',
        'name' : 'Cliente 2',
        'value' : 10
    }
}

if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password'] : 
    print('Conta válida')
else: 
    print('Conta inválida')