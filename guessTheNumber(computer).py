import random

def guessNumberCom():
    low = int(input('Enter a low number: '))
    high = int(input('Enter a high number: '))
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        #guess = random.randint(low, high)
        attempts += 1

        answer = input(f'>>computer guessed {guess} is it correct, low or high(c/l/h)? ').lower()
        if answer == 'c':
            break

        elif answer == 'l':
            low = guess + 1

        elif answer == 'h':
            high = guess - 1

        else:
            print('Invalid input')
            continue

    else:
        print('<< arithmetic error >>')
        print('please enter numbers in right order')
        return guessNumberCom()

    return guess, attempts

number, attempts = guessNumberCom()
print(f'*** Computer guessed "{number}" in {attempts} tries')