import random

colors = ['B', 'R', 'G', 'Y', 'W']
pallete = random.choices(colors, k=4)
print(pallete)
chances = 5

while chances > 0:
    guess = [color.upper() for color in input(f'guess a 4-colored pallete from:{colors}; (with seperations) >>> ').split()]
    chances -= 1
    if list(filter(lambda x: x not in colors, guess)) or len(guess) != 4:
        print('you should enter a 4-colored pallete from the list')
        print(f'you have {chances} chances left')
        continue

    if guess == pallete:
        print('you correctly guessed the pallete')
        break

    if chances == 0:
        print('you lost')
        print(f'the pallete was {pallete}')
        break

    correct_positions = 0
    incorrect_positions = 0
    temp = pallete.copy()
    for i in range(4):
        if guess[i] == pallete[i]:
            correct_positions += 1

        elif guess[i] in temp:
            incorrect_positions += 1
            temp.remove(guess[i])


    print(f'Correct Positions: {correct_positions} | Incorrect Positions: {incorrect_positions}')
    print(f'you have {chances} chances left')
