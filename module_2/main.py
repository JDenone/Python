import getpass
import os

while True : 
    print('****************************************')
    print('*** School of Net - Caixa Eletrônico ***')
    print('****************************************')

    #   o input recebe os dados da iteração e salva como uma string e é necessário ter uma variável para receber 
    # os dados da iteração
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')
    #print(account_typed)
    #print(password_typed)

    accounts_list = {
        '0001-02': {
            'password' : '123456',
            'name' : 'Cliente 1',
            'value' : 100,
            'admin' : False
        },
        '0002-02' : {
            'password' : '456123',
            'name' : 'Cliente 2',
            'value' : 50,
            'admin' : False
        },
        '1111-11' : {
            'password' : '999999',
            'name' : 'Admin',
            'value' : 1000,
            'admin' : True
        }
    }

    money_slips = {
        '20' : 5,
        '50' : 5,
        '100' : 5
    }

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password'] : 
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("****************************************")
        print("*** School of Net - Caixa Eletrônico ***")
        print('****************************************')
        print('1 - Saldo')

        # if accounts_list[account_typed]['admin'] == True :  ---> esse parametro True, já está condicionado na variáevel, então não precisa ser testado
        if accounts_list[account_typed]['admin'] : 
            print('10 - incluir cédulas')
        option_typed = input('Escolha uma das opções acima: ')
        if option_typed == '1' : 
            #print('Seu saldo em conta é de: ' + accounts_list[account_typed]['value'])
            # o caractere % funciona como uma tag ou token, que pode ser posicionado em qualquer ligar da string
            print('Seu saldo em conta é de: %s' % accounts_list[account_typed]['value'])
        elif option_typed == '10' and accounts_list[account_typed]['admin'] : 
            amount_typed = input('Digite a quantidade de cédulas: ')
            money_bill_typed = input('Digite a cédula a ser inserida: ')

            # Resultado da inclusão de cédulas
            money_slips[money_bill_typed] =  money_slips[money_bill_typed] + int(amount_typed)
            print(money_slips)
    else: 
        print('Conta inválida')

    input('Pressione <ENTER> para continuar')
    # o operador Ternário inverte a ordem, mas tem a mesma função da expressão abaixo
    os.system('cls' if os.name == 'nt' else 'clear') 
    
    #if os.name == 'nt' :
    #    os.system('cls')
    #else:
    #    os.system('clear')
    