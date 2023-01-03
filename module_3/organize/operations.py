import getpass
from organize.bank_account_variables import accounts_list, money_slips

def do_operation(option_typed, account_auth):
    if option_typed == '1':
        show_balance(account_auth)
    elif option_typed == '10' and accounts_list[account_auth]['admin'] : 
        insert_money_slips()
    elif option_typed == '2':
        whithdraw(account_auth)

def show_balance(account_auth):
    print('Seu saldo em conta é de: %s' % accounts_list[account_auth]['value'])

def insert_money_slips():
    amount_typed = input('Digite a quantidade de cédulas: ')
    money_bill_typed = input('Digite a cédula a ser inserida: ')
    money_slips[money_bill_typed] += int(amount_typed)
    print(money_slips)

def whithdraw(account_auth):
    value_typed = input('Digite o valor a ser sacado: ')

    if int(value_typed) > accounts_list[account_auth]['value'] :
        print ('Valor não disponível em conta')
    else:
        money_slips_users = {}
        value_int = int(value_typed)

        if value_int // 100 > 0 and value_int // 100 <= money_slips['100'] :
            money_slips_users['100'] = value_int // 100
            value_int -= value_int // 100 * 100

        if value_int // 50 > 0 and value_int // 50 <= money_slips['50'] :
            money_slips_users['50'] = value_int // 50
            value_int -= value_int // 50 * 50

        if value_int // 20 > 0 and value_int // 20 <= money_slips['20'] :
            money_slips_users['20'] = value_int // 20
            value_int -= value_int // 20 * 20  

        if value_int != 0 :
            print('O Caixa não tem cédulas disponíveis para este valor.')  

        else :
            for money_bill in money_slips_users :
                money_slips[money_bill] -= money_slips_users[money_bill]
                
            print('Retire suas notas: ')
            print(money_slips_users)

def auth_account():
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password'] : 
        return account_typed
    else:
        return False

def get_menu_option_typed(account_auth):
    print('1 - Saldo')
    print('2 - Saque')

    if accounts_list[account_auth]['admin'] : 
        print('10 - incluir cédulas')
    return input('Escolha uma das opções acima: ')