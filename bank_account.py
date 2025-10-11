


balance = 100
def show_balance(add=0, sub=0):
    global balance
    balance = balance + add - sub
    return balance

def deposite():
    amount = input("Enter amount to deposite: ")
    if not amount.isdigit():
        print("Please enter a valid amount.")
        return deposite()
    amount = float(amount)

    show_balance(add=amount)


def withdraw():
    amount = input("Enter amount to withdraw: ")
    if not amount.isdigit():
        print("Please enter a valid amount.")
        return withdraw()
    amount = float(amount)
    if amount > show_balance():
        print('you do not have enough to withdraw')
        return withdraw()
    show_balance(add=0, sub=amount)


print('Welcome to bank account app')
while True:
    print('Which operation would you like to do?')
    print('1. show balance')
    print('2. deposite')
    print('3. withdraw')
    print('4. exit')
    operation = input('>> ')

    if operation == '1':
        print(f'Your balance is ${show_balance()}')
    elif operation == '2':
        deposite()
        print(f'Your balance is ${show_balance()}')
    elif operation == '3':
        withdraw()
        print(f'Your balance is ${show_balance()}')
    else:
        print('Have a nice day!')
        break