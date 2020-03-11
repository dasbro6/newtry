def newusers():
    print('n')
    name = input('enter a name: ')
    while True:
        if name in dict_user:
            name = input('enter again:')
        else:
            password = input('set the password:')
            dict_user[name] = password
            return


def oldusers():
    print('o')
    name = input('Enter the username : ')
    password = input('Enter the password : ')
    try:
        if password == dict_user[name]:
            print(name, 'welcome back ')
        else:
            print('login incorrect')
    except:
        print('login incorrect')


def login():
    while True:
        option = input('''
                 (N)ew User Login
                 (O)ld User Login
                 (E)xit
        Enter the option: ''',)
        if option == 'N':
            newusers()
            return
        elif option == 'O':
            oldusers()
            return
        elif option == 'E':
            break
        else:
            continue


if __name__ == '__main__':
    dict_user = {}
    with open('login.txt','r+') as f:
        for line in f.readlines():
            line = line.strip()
            k = line.split(' ')[0]
            v = line.split(' ')[1]
            dict_user[k] = v
        print(type(dict_user))
    login()
    with open('login.txt', 'w+') as f:
        for k, v in dict_user.items():
            f.write(str(k) + ' ' + str(v) + '\n')