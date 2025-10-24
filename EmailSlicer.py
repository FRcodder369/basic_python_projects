
emails = input("Enter your emails: ").split()

for i in emails:
    name, rest = i.split('@')
    print(f'You have an email from "{name}"')

