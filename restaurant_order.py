menu = {'tea':int(3),
        'pizza':int(9),
        'soup':int(4),
        'raviolli':int(6),
        'coffee':int(4),
        'cepelini':int(7)
}

def restaurant():
    total = []
    while True:
        clorder = input('Whats your order?: ')
        if not clorder:
            print(f'Total amount of Your order is: {sum(total)}')
            break
        elif clorder in menu:
            total.append(menu[clorder])
            print(f'{clorder} costs {menu[clorder]}, total is {sum(total)}')
        elif clorder not in menu:
            print('There is no such a dish. Please choose it from the menu: ')
        
restaurant()