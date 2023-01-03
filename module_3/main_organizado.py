from organize.operations import auth_account, get_menu_option_typed, do_operation
from organize.utils import clear, header

def main() : 
    header()
    account_auth = auth_account()
    
    if account_auth:
        clear()
        header()

        option_typed = get_menu_option_typed(account_auth)
        do_operation(option_typed, account_auth)
    else: 
        print('Conta inválida')

while True :
    
    main()
    input('Pressione <ENTER> para continuar')
    clear()