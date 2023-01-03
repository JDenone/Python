import os

def clear() :
    os.system('cls' if os.name == 'nt' else 'clear')

def header() :
    print('****************************************')
    print('*** School of Net - Caixa Eletrônico ***')
    print('****************************************')