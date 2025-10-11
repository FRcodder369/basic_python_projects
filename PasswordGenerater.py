import random
import string


def password_generator(min_length, number=True, special=True):
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special:
        characters += punctuation


    psw = ''
    has_number = False
    has_special = False
    meets_criteria = False
    while not meets_criteria or len(psw) < min_length:
        new_char = random.choice(characters)
        psw += new_char

        if new_char in digits:
            has_number = True
        elif new_char in punctuation:
            has_special = True

        meets_criteria = True
        if number:
            meets_criteria = meets_criteria and has_number
        if special:
            meets_criteria = meets_criteria and has_special

    return psw

min_length = int(input('Enter minimum password length: '))
has_numbers = input('Do you want to use numbers? (y/n): ').lower() == 'y'
has_specials = input('Do you want to use special characters? (y/n): ').lower() == 'y'

print(f'your password is {password_generator(min_length, has_numbers, has_specials)}')