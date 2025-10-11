import time
import random

def spin():
    symbols = ['🍒', '🍋', '🎃', '🔔', '💸']
    rows = random.choices(symbols, k=3)
    return rows

def get_prize(rows):
    prizes = {'🍒': 3, '🍋': 5, '🎃': 7, '🔔': 10, '💸': 25}
    prize = 0
    if rows[0] == rows[1] == rows[2]:
        prize = prizes[rows[0]] * 3
    return prize


balance = 100
def play():
    global balance
    bet = int(input('How much money would you like to bet? '))
    if 0 > bet > balance:
        print('Sorry, you can\'t bet more than you have or under 1')
        return play()

    balance -= bet
    print('Spinning...\n')
    rows = spin()

    print(*rows, sep=' | ')
    prize = get_prize(rows)
    if prize > 0:
        print(f'you win ${prize}')

    balance += prize
    print(f'Your balance is ${balance}')




print('*******************************************')
print('Welcome to Py Slot Machine')
print('Symbols are: 🍒, 🍋, 🎃, 🔔, 💸')
print('*******************************************')

playing = True
while playing:
    play()
    next = input('Press enter to play again enter anything else to quit ')
    if next == '':
        continue
    else:
        print('Thank you for playing!')
        playing = False
