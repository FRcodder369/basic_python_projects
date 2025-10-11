import random

symbols = {'r': '👊', 'p': '✋', 's': '🖖'}

def winner(player, computer):
    options = {
        ('r', 's'): player,
        ('p', 'r'): player,
        ('s', 'p'): player,
        ('s', 'r'): computer,
        ('r', 'p'): computer,
        ('p', 's'): computer,
        ('r', 'r'): 'tie',
        ('p', 'p'): 'tie',
        ('s', 's'): 'tie'
    }
    return options[(player, computer)]



def play():
    wins = 0
    loses = 0
    ties = 0

    while True:
        user = input('rock, paper, scissors?(r/p/s): ').lower()
        computer = random.choice(list(symbols.keys()))
        print(f'user: {symbols[user]}')
        print(f'computer: {symbols[computer]}')

        status = winner(user, computer)
        if status == user:
            print('you win')
            wins += 1
        elif status == computer:
            print('you lose')
            loses += 1
        elif status == 'tie':
            print('tie')
            ties += 1

        print(f'wins {wins} | loses {loses} | ties {ties}')
        next_play = input('Do you want to play again?(y/n): ').lower()
        if next_play == 'y':
            continue
        else:
            print('Thanks for playing!')
            return 0

play()






