import random

print("*** Welcome to Guess the Number Game ***")

def guess_number():
    low = 1
    high = 100
    attempts = 0
    number = random.randrange(low, high+1)

    while True:
        guess = int(input(f'Guess a number between {low} and {high}: '))
        attempts += 1

        if guess == number:
            break
        elif guess < number:
            print('Too low')
            if low < guess:
                low = guess + 1
        elif guess > number:
            print('Too high')
            if high > guess:
                high = guess - 1

    return number, attempts
number, attempts = guess_number()
print(f'Congratulations! You guessed the number <{number}> in {attempts} tries.')