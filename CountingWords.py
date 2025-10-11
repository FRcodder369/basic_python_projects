from collections import Counter

contents = ''
with open('test.txt', 'r') as file:
    contents = file.read().lower()

word_count = Counter(contents.split())
print(f'{"WORD":>7}{"COUNT":>7}')

for word, count in word_count.items():
    print(f'{word:>7}{count:>7}')

print(f'>>Number of unique words: {len(word_count)}')
print(f'>>Number of total words: {sum(word_count.values())}')
