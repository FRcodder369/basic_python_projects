import random

def pick_word():
    words = ['computer', 'arificial', 'intelligence', 'teacher', 'mechanic', 'rainbow', 'coffeeshop']
    word = random.choice(words)
    return word

def hoder(word):
    return ["_"] * len(word)


def hint(word):
    length = len(word)
    return random.randrange(length)

def show_hangman(mistakes):
    hangman_art = {
        0: ('+-----+    \n'
            '|          \n'
            '|          \n'
            '|          \n'
            '|___\n'),
        1: ('+-----+    \n'
            '|     o    \n'
            '|          \n'
            '|          \n'
            '|___\n'),
        2: ('+-----+    \n'
            '|     o    \n'
            '|     |    \n'
            '|          \n'
            '|___\n'),
        3: ('+-----+    \n'
            '|     o    \n'
            '|    /|    \n'
            '|          \n'
            '|___\n'),
        4: ('+-----+    \n'
            '|     o    \n'
            '|    /|\\  \n'
            '|          \n'
            '|___\n'),
        5: ('+-----+    \n'
            '|     o    \n'
            '|    /|\\  \n'
            '|    /     \n'
            '|___\n'),
        6: ('+-----+    \n'
            '|     o    \n'
            '|    /|\\  \n'
            '|    / \\  \n'
            '|___\n'),
    }

    return hangman_art[mistakes]


def main():
    word = pick_word()
    word_holder = hoder(word)
    mistakes = 0
    hint_count = 2


    while mistakes < 6 and '_' in word_holder:
        print(word_holder)
        if hint_count > 0:
            print(f'?? you have {hint_count} hint left')
            print('if you want a hint type "?"')

        guess = input("Guess a letter: ").lower()
        if guess == word:
            break

        elif guess == '?':
            while True:
                number = hint(word)
                if word_holder[number] == '_':
                    word_holder[number] = word[number]
                    hint_count -= 1
                    break

        elif guess in word:
            print(f'correct {guess} is in the word')
            for i in range(len(word)):
                if guess == word[i]:
                    word_holder[i] = guess

        elif not guess in word:
            print(f'wrong {guess} is not in the word')
            mistakes += 1
            print(f'You have {6 - mistakes} chances left')

    if mistakes == 6:
        print('GAME OVER')

    else:
        print('you won')

    print(show_hangman(mistakes))




if __name__ == '__main__':
    main()