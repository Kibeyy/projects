while True:
    print('Banking System')
    command = input('TO REGISTER A NEW ACCOUNT, ENTER 1\nTO LOGIN, ENTER 2\n')

    if command == '1':
        print('Hello, To register an account please provide us with:')
        while True:
            # accepting input from the user to create an account
            firstname = input('FIRST NAME: ')
            secname = input('SECOND NAME: ')
            try:
                idno = int(input('ID NUMBER: '))
            except ValueError:
                print('ID Number can only be in digits! Try again')
                continue
            password = input('NEW PASSWORD: ')
            print('Account registered successfully, You can now log in.')
            # storing the user data in a file
            with open('clients.txt', 'w') as docs:
                docs.write(firstname.title() + ' ' + secname.title() + '\n' + str(idno) + '\n' + password + '\n')
            break

    elif command == '2':
        while True:
            print('Welcome back, To login enter your :')
            username = input('USERNAME: ')
            with open('clients.txt', 'r') as userconf:
                confirmation = userconf.readlines()
                conf = [item.strip('\n') for item in confirmation]
                if username == conf[0]:
                    password = input('PASSWORD: ')
                    if password == conf[2]:
                        print('LOGIN SUCCESSFUL')
                        with open('bankes.txt', 'r') as balance_file:
                            balance = int(balance_file.read())

                        while True:  # Loop for the logged-in user
                            request = input('''To check account balance, Enter 1
To deposit cash to your account, Enter 2
To withdraw cash from your account, Enter 3
To log out, Enter 4\n''')

                            if request == '1':
                                print(f'Your account balance is {balance}')

                            elif request == '2':
                                depo = int(input('Enter the amount to deposit: '))
                                balance += depo
                                with open('bankes.txt', 'w') as deposit:
                                    deposit.write(str(balance))
                                print(f'Successfully deposited {depo} Shillings')

                            elif request == '3':
                                withdraw = int(input('Enter amount you wish to withdraw: '))
                                if withdraw <= balance:
                                    balance -= withdraw
                                    with open('bankes.txt', 'w') as withdraw_file:
                                        withdraw_file.write(str(balance))
                                    print(f'Withdrawal successful. Your new balance is: {balance}')
                                else:
                                    print('Insufficient balance for withdrawal')

                            elif request == '4':
                                print('Logged out')
                                break  # Exit the inner loop (logged-in user)

                            else:
                                print('Invalid input. Please select a valid option.')

                        break  # Exit the outer loop (login prompt)
                    else:
                        print('Wrong password. Try again')
                        break  # Exit the outer loop (login prompt)
                else:
                    print('User not found. Please register a new account')
                    break  # Exit the outer loop (login prompt)

    else:
        print('Please reply using the given commands')
